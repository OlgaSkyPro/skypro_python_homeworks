from string_utils import StringUtils
import pytest

@pytest.mark.positive_test
def test_capitilize_positive1():
    string_test = StringUtils()
    res = string_test.capitilize("olga")
    assert res == "Olga"

@pytest.mark.positive_test
def test_capitilize_positive2():
    string_test = StringUtils()
    res = string_test.capitilize("olga 13 feb 1960")
    assert res == "Olga 13 feb 1960"

def test_capitilize_negative1():
    string_test = StringUtils()
    res = string_test.capitilize("")
    assert res == ""

def test_capitilize_negative2():
    string_test = StringUtils()
    res = string_test.capitilize(" ")
    assert res == " "

def test_capitilize_negative3():
    string_test = StringUtils()
    with pytest.raises(AttributeError):
        res = string_test.capitilize(1000)
    
@pytest.mark.positive_test
def test_trim_positive1():
    trim_test= StringUtils()
    res= trim_test.trim ("   Olga")
    assert res == "Olga"

@pytest.mark.positive_test
def test_trim_positive2():
    trim_test= StringUtils()
    res= trim_test.trim ("   Olga 13 feb 1960")
    assert res == "Olga 13 feb 1960"

def test_trim_negative1():
    trim_test= StringUtils()
    res= trim_test.trim ("Olga")
    assert res == "Olga"

def test_trim_negative2():
    trim_test= StringUtils()
    with pytest.raises(AttributeError):
        res= trim_test.trim (1000)

@pytest.mark.positive_test
def test_to_list_positive():
    to_list__test = StringUtils()
    res = to_list__test.to_list ("O,l,g,a")
    assert res == ["O","l", "g", "a"]

def test_to_list_negative1():
    to_list__test = StringUtils()
    res = to_list__test.to_list ("")
    assert res == []

def test_to_list_negative2():
    to_list__test = StringUtils()
    with pytest.raises(AttributeError):
        res = to_list__test.to_list (1000)

@pytest.mark.positive_test
def test_contains_positive1():
    contains_test= StringUtils()
    res= contains_test.contains ("Olga", "a")
    assert res == True

@pytest.mark.positive_test
def test_contains_positive2():
    contains_test= StringUtils()
    res= contains_test.contains ("Olga 13 feb 1960", "a")
    assert res == True

def test_contains_negative1():
    contains_test= StringUtils()
    res= contains_test.contains ("", "")
    assert res == True

def test_contains_negative2():
    contains_test= StringUtils()
    with pytest.raises(AttributeError): 
        res= contains_test.contains (1000, 0)
    
@pytest.mark.positive_test
def test_delete_symbol_positive1():
    del_simbol_test= StringUtils()
    res= del_simbol_test.delete_symbol ("OlgaK", "K")
    assert res == "Olga"

@pytest.mark.positive_test
def test_delete_symbol_positive2():
    del_simbol_test= StringUtils()
    res= del_simbol_test.delete_symbol ("OlgaK 13 feb 1960", "K")
    assert res == "Olga 13 feb 1960"

def test_delete_symbol_negative1():
    del_simbol_test= StringUtils()
    res= del_simbol_test.delete_symbol ("", "")
    assert res == ""

def test_delete_symbol_negative2():
    del_simbol_test= StringUtils()
    with pytest.raises(AttributeError):
        res= del_simbol_test.delete_symbol (1000, 0)
    
@pytest.mark.positive_test
def test_starts_with_positive1():
    starts_with_test= StringUtils()
    res= starts_with_test.starts_with ("Olga", "O")
    assert res == True

@pytest.mark.positive_test
def test_starts_with_positive2():
    starts_with_test= StringUtils()
    res= starts_with_test.starts_with ("Olga 13 feb 1960", "O")
    assert res == True

def test_starts_with_negative1():
    starts_with_test= StringUtils()
    res= starts_with_test.starts_with ("", "")
    assert res == True

def test_starts_with_negative2():
    starts_with_test= StringUtils()
    with pytest.raises(AttributeError):
        res= starts_with_test.starts_with (1000, 1)
    
@pytest.mark.positive_test
def test_end_with_positive1():
    end_with_test= StringUtils()
    res= end_with_test.end_with ("Olga", "a")
    assert res == True

@pytest.mark.positive_test
def test_end_with_positive2():
    end_with_test= StringUtils()
    res= end_with_test.end_with ("Olga 13 feb 1960", "0")
    assert res == True

def test_end_with_negative1():
    end_with_test= StringUtils()
    res= end_with_test.end_with ("", "")
    assert res == True

def test_end_with_negative2():
    end_with_test= StringUtils()
    with pytest.raises(AttributeError):
        res= end_with_test.end_with (1000, 0)
    
@pytest.mark.positive_test
def test_is_empty_positive1():
    is_empty_test= StringUtils()
    res= is_empty_test.is_empty ("Olga")
    assert res == False

@pytest.mark.positive_test
def test_is_empty_positive2():
    is_empty_test= StringUtils()
    res= is_empty_test.is_empty ("Olga 13 feb 1960")
    assert res == False

def test_is_empty_negative1():
    is_empty_test= StringUtils()
    res= is_empty_test.is_empty ("")
    assert res == True

def test_is_empty_negative2():
    is_empty_test= StringUtils()
    with pytest.raises(AttributeError):
        res= is_empty_test.is_empty (1000)
    

@pytest.mark.positive_test
def test_list_to_string_positive():
    list_to_string_test = StringUtils()
    res = list_to_string_test.list_to_string (["O", "l", "g", "a"])
    assert res == "O, l, g, a"

def test_list_to_string_negative1():
    list_to_string_test = StringUtils()
    res = list_to_string_test.list_to_string ([])
    assert res == ""

def test_list_to_string_negative2():
    list_to_string_test = StringUtils()
    res = list_to_string_test.list_to_string ([1,0,0,0])
    assert res == "1, 0, 0, 0"
    
