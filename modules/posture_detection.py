import cv2
import mediapipe as mp
import streamlit as st
import time
import tempfile
import numpy as np

from utils.angles import calculate_angle

mp_pose = mp.solutions.pose
mp_draw = mp.solutions.drawing_utils


# ---------------- FRAME PROCESSING ----------------
def process_frame(frame, pose, view):
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = pose.process(image)

    metrics = {
        "score": 0,
        "posture": view,
        "angles": {},
        "feedback": ["No pose detected"]
    }

    if results.pose_landmarks:
        lm = results.pose_landmarks.landmark

        # landmarks
        LS = [lm[11].x, lm[11].y]
        RS = [lm[12].x, lm[12].y]
        LE = [lm[13].x, lm[13].y]
        RE = [lm[14].x, lm[14].y]
        LW = [lm[15].x, lm[15].y]
        RW = [lm[16].x, lm[16].y]
        LH = [lm[23].x, lm[23].y]
        RH = [lm[24].x, lm[24].y]
        LK = [lm[25].x, lm[25].y]
        RK = [lm[26].x, lm[26].y]
        LA = [lm[27].x, lm[27].y]
        RA = [lm[28].x, lm[28].y]

        score = 100
        feedback = []
        angles = {}

        # ---------- FRONT ----------
        if view == "Front View":
            shoulder_diff = abs(LS[1] - RS[1])
            stance_width = abs(LA[0] - RA[0])

            angles["Shoulder Difference"] = round(shoulder_diff, 3)
            angles["Stance Width"] = round(stance_width, 3)

            if shoulder_diff > 0.03:
                feedback.append("Level your shoulders")
                score -= 15

            if stance_width < 0.08:
                feedback.append("Widen your stance")
                score -= 10

        # ---------- RIGHT ----------
        elif view == "Right Side":
            elbow = calculate_angle(RS, RE, RW)
            hip = calculate_angle(RS, RH, RK)

            angles["Right Elbow"] = int(elbow)
            angles["Right Hip"] = int(hip)

            if elbow < 160:
                feedback.append("Straighten right arm")
                score -= 20

            if hip < 170:
                feedback.append("Straighten spine")
                score -= 15

        # ---------- LEFT ----------
        elif view == "Left Side":
            elbow = calculate_angle(LS, LE, LW)
            hip = calculate_angle(LS, LH, LK)

            angles["Left Elbow"] = int(elbow)
            angles["Left Hip"] = int(hip)

            if elbow < 160:
                feedback.append("Straighten left arm")
                score -= 20

            if hip < 170:
                feedback.append("Straighten spine")
                score -= 15

        # ---------- BACK ----------
        elif view == "Back View":
            shoulder_diff = abs(LS[1] - RS[1])
            elbow_diff = abs(LE[1] - RE[1])

            angles["Shoulder Difference"] = round(shoulder_diff, 3)
            angles["Elbow Difference"] = round(elbow_diff, 3)

            if shoulder_diff > 0.03:
                feedback.append("Keep shoulders level")
                score -= 15

            if elbow_diff > 0.05:
                feedback.append("Keep elbows aligned")
                score -= 15

        if not feedback:
            feedback = ["Excellent posture ✅"]

        score = max(score, 0)

        metrics = {
            "score": score,
            "posture": view,
            "angles": angles,
            "feedback": feedback
        }

        # draw only skeleton
        mp_draw.draw_landmarks(
            frame,
            results.pose_landmarks,
            mp_pose.POSE_CONNECTIONS
        )

    return frame, metrics


# ---------------- DISPLAY METRICS ----------------
def show_metrics(metrics):
    st.metric("Posture Score", metrics["score"])

    st.subheader("Posture Type")
    st.write(metrics["posture"])

    st.subheader("Angles")
    st.json(metrics["angles"])

    st.subheader("Feedback")
    for f in metrics["feedback"]:
        st.write(f"• {f}")


# ---------------- MAIN ----------------
def run():
    st.title("KARNA - Posture Detection 🏹")

    view = st.selectbox(
        "Camera/View Angle",
        ["Front View", "Right Side", "Left Side", "Back View"]
    )

    mode = st.radio(
        "Select Mode",
        ["Live Camera", "Upload Image", "Upload Video"]
    )

    pose = mp_pose.Pose()

    # ---------- LIVE ----------
    if mode == "Live Camera":

        if "run_cam" not in st.session_state:
            st.session_state.run_cam = False

        if st.button("Start Camera"):
            st.session_state.run_cam = True

        if st.button("Stop Camera"):
            st.session_state.run_cam = False

        if st.session_state.run_cam:
            cap = cv2.VideoCapture(0)

            left, right = st.columns([2, 1])
            frame_placeholder = left.empty()
            metric_placeholder = right.empty()

            while cap.isOpened() and st.session_state.run_cam:
                ret, frame = cap.read()

                if not ret:
                    st.error("Camera error")
                    break

                frame, metrics = process_frame(frame, pose, view)

                frame_placeholder.image(frame, channels="BGR")

                with metric_placeholder.container():
                    show_metrics(metrics)

                time.sleep(0.03)

            cap.release()

    # ---------- IMAGE ----------
    elif mode == "Upload Image":

        uploaded_file = st.file_uploader(
            "Upload Image",
            type=["jpg", "png", "jpeg"]
        )

        if uploaded_file:
            file_bytes = uploaded_file.read()
            np_arr = np.frombuffer(file_bytes, np.uint8)

            frame = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

            frame, metrics = process_frame(frame, pose, view)

            left, right = st.columns([2, 1])

            with left:
                st.image(frame, channels="BGR")

            with right:
                show_metrics(metrics)

    # ---------- VIDEO ----------
    elif mode == "Upload Video":

        uploaded_file = st.file_uploader(
            "Upload Video",
            type=["mp4", "mov", "avi"]
        )

        if uploaded_file:
            tfile = tempfile.NamedTemporaryFile(delete=False)
            tfile.write(uploaded_file.read())

            cap = cv2.VideoCapture(tfile.name)

            left, right = st.columns([2, 1])
            frame_placeholder = left.empty()
            metric_placeholder = right.empty()

            while cap.isOpened():
                ret, frame = cap.read()

                if not ret:
                    break

                frame, metrics = process_frame(frame, pose, view)

                frame_placeholder.image(frame, channels="BGR")

                with metric_placeholder.container():
                    show_metrics(metrics)

                time.sleep(0.03)

            cap.release()