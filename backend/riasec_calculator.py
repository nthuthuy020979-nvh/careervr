import json

def calculate_riasec(answers_json):
    """
    Calculate RIASEC scores from 50 questions.
    
    Part 1: RIASEC Interests (Q1-24, 4 per category)
    - Q1-4: R (Realistic)
    - Q5-8: I (Investigative)
    - Q9-12: A (Artistic)
    - Q13-16: S (Social)
    - Q17-20: E (Enterprising)
    - Q21-24: C (Conventional)
    
    Part 2: Skills/Abilities (Q25-38, mixed RIASEC)
    Part 3: Values (Q39-46, mixed RIASEC)
    Part 4: Practical Conditions (Q47-50, mixed RIASEC)
    """
    
    # Parse input
    answers = json.loads(answers_json) if isinstance(answers_json, str) else answers_json
    
    if len(answers) != 50:
        raise ValueError("khong_du_50_cau")
    
    # =====================
    # PART 1: RIASEC BASE (1-24)
    # =====================
    R = sum(answers[0:4])      # Q1-4
    I = sum(answers[4:8])      # Q5-8
    A = sum(answers[8:12])     # Q9-12
    S = sum(answers[12:16])    # Q13-16
    E = sum(answers[16:20])    # Q17-20
    C = sum(answers[20:24])    # Q21-24
    
    # =====================
    # PART 2: SKILLS (Q25-38) - ADD TO BASE
    # =====================
    R += answers[24] + answers[28] + answers[29]  # Q25, Q29, Q30
    I += answers[25] + answers[30] + answers[31]  # Q26, Q31, Q32
    A += answers[32] + answers[33] + answers[41]  # Q33, Q34, Q42
    S += answers[27] + answers[34] + answers[35]  # Q28, Q35, Q36 (NOTE: Q28 is giao tiếp but mapped to S here)
    E += answers[26] + answers[36] + answers[37]  # Q27, Q37, Q38 (NOTE: Q27 is máy tính but mapped to E here)
    C += answers[38] + answers[39] + answers[44]  # Q39, Q40, Q45
    
    # =====================
    # TOTAL RIASEC SCORES
    # =====================
    riasec_scores = {
        "R": R,
        "I": I,
        "A": A,
        "S": S,
        "E": E,
        "C": C
    }
    
    # =====================
    # TOP 3
    # =====================
    top_3_riasec = sorted(
        riasec_scores,
        key=riasec_scores.get,
        reverse=True
    )[:3]
    
    # =====================
    # RETURN - MATCHES DIFY VARIABLES
    # =====================
    return {
        "full_scores": riasec_scores,
        "score_R": R,
        "score_I": I,
        "score_A": A,
        "score_S": S,
        "score_E": E,
        "score_C": C,
        "top_1_type": top_3_riasec[0],
        "top_3_list": top_3_riasec
    }


# Example usage
if __name__ == "__main__":
    # Sample 50 answers (all 3s)
    sample_answers = [3] * 50
    result = calculate_riasec(json.dumps(sample_answers))
    print(json.dumps(result, indent=2))
