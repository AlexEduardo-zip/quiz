import pytest
from model import Question


def test_create_question():
    question = Question(title='q1')
    assert question.id != None

def test_create_multiple_questions():
    question1 = Question(title='q1')
    question2 = Question(title='q2')
    assert question1.id != question2.id

def test_create_question_with_invalid_title():
    with pytest.raises(Exception):
        Question(title='')
    with pytest.raises(Exception):
        Question(title='a'*201)
    with pytest.raises(Exception):
        Question(title='a'*500)

def test_create_question_with_valid_points():
    question = Question(title='q1', points=1)
    assert question.points == 1
    question = Question(title='q1', points=100)
    assert question.points == 100

def test_create_choice():
    question = Question(title='q1')
    
    question.add_choice('a', False)

    choice = question.choices[0]
    assert len(question.choices) == 1
    assert choice.text == 'a'
    assert not choice.is_correct

def test_question_defaults():
    q = Question("Title")
    assert q.points == 1
    assert q.max_selections == 1

def test_question_custom_values():
    q = Question("Title", 5, 3)
    assert q.points == 5
    assert q.max_selections == 3

def test_add_choice():
    q = Question("Title")
    c = q.add_choice("Option", True)
    assert c.text == "Option"
    assert c.is_correct
    assert len(q.choices) == 1

def test_remove_choice():
    q = Question("Title")
    c = q.add_choice("Option", False)
    q.remove_choice_by_id(c.id)
    assert len(q.choices) == 0

def test_remove_nonexistent_choice():
    q = Question("Title")
    with pytest.raises(Exception):
        q.remove_choice_by_id(999)

def test_select_correct_choice():
    q = Question("Title")
    c = q.add_choice("Right", True)
    assert q.select_choices([c.id]) == [c.id]

def test_select_wrong_choice():
    q = Question("Title")
    c = q.add_choice("Wrong", False)
    assert q.select_choices([c.id]) == []

def test_max_selection_limit():
    q = Question("Title", max_selections=1)
    c1 = q.add_choice("Opt1", True)
    c2 = q.add_choice("Opt2", True)
    with pytest.raises(Exception):
        q.select_choices([c1.id, c2.id])

def test_set_correct_choices():
    q = Question("Title")
    c = q.add_choice("Opt", False)
    q.set_correct_choices([c.id])
    assert c.is_correct

def test_create_invalid_choice():
    q = Question("Title")
    with pytest.raises(Exception):
        q.add_choice("", False)