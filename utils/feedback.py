from config import IDEAL_ANGLES

def get_feedback(elbow, shoulder):
    feedback = []

    if elbow < 160:
        feedback.append("Raise your elbow higher")

    if shoulder < 150:
        feedback.append("Align your shoulders")

    if not feedback:
        return ["Perfect posture ✅"]

    return feedback


def posture_score(elbow, shoulder):
    score = 100
    score -= abs(IDEAL_ANGLES["elbow"] - elbow)
    score -= abs(IDEAL_ANGLES["shoulder"] - shoulder)
    return max(score, 0)