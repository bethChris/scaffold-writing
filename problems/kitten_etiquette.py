###############################################################################
#### DO NOT EDIT THIS SECTION
###############################################################################
from typing import Dict, Any, List, Tuple, Optional
from shared_utils import set_weighted_score_data
from scaffolded_writing.cfg import ScaffoldedWritingCFG
from scaffolded_writing.student_submission import StudentSubmission
from shared_utils import grade_question_parameterized

def generate(data: Dict[str, Any]) -> None:
    data["params"]["subproblem_definition_cfg"] = PROBLEM_CONFIG.to_json_string()

def grade(data: Dict[str, Any]) -> None:
    grade_question_parameterized(data, "subproblem_definition", grade_statement)
    set_weighted_score_data(data)

###############################################################################
#### DO NOT EDIT ABOVE HERE, ONLY EDIT BELOW
###############################################################################

statement = 'Assume you encounter a small kitten.' + \
    'The creature approaches you and meows. What is your next move?'

PROBLEM_CONFIG = ScaffoldedWritingCFG.fromstring(f"""
    START -> VERB SUBJECT PART ADVERB END | VERB "it" ADVERB END
    VERB -> "Boop" | "Kick" | "Pet" 
    SUBJECT -> "the kittens" | "its" | "the rocks"
    PART -> "head" | "tail" | "ears" | "nose" | "toes" | "eyes"
    ADVERB -> "quickly" | "softly" | "gently" | EPSILON
    END -> "." | "!"
    EPSILON -> 
""")

def grade_statement(tokens: List[str]) -> Tuple[bool, Optional[str]]:
    submission = StudentSubmission(tokens, PROBLEM_CONFIG)

    if submission.does_path_exist("SUBJECT", "the rocks"):
        return False, '...there are no rocks in this question, ' + \
            'try to stay focused on the questions subject.'

    if submission.does_path_exist("VERB", "Kick"):
        return False, 'Kicking a harmless kitten is not advised' + \
            ' and is usually considered unethical.'

    if submission.does_path_exist('PART', 'eyes'):
        return False, 'While giving the kitten some affection is great, ' + \
            'aiming for the eyes of a kitten may hurt it.'
    
    if submission.does_path_exist('PART', 'tail'):
        return False, 'Beware the tail. This approach will likely end in pain... for you.'
    
    if submission.does_path_exist('ADVERB', "quickly"):
        return False, 'Approaching a ' + \
        'kitten too quickly may scare it away.'
    
    return True, None


