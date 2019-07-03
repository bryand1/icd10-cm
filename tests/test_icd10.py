import icd10


def test_exists():
    assert icd10.exists("T50.B")
    assert icd10.exists("T50B")       # Omit the period
    assert not icd10.exists("A99.8")
    assert icd10.exists("Z01.4")


def test_find_salmonella():
    dx = icd10.find("A02.1")
    assert isinstance(dx, icd10.ICD10)
    assert dx.code == "A021"
    assert dx.billable
    assert dx.description == "Salmonella sepsis"
    assert not dx.categorical  # Categorical codes are by definition not billable
    assert dx.block == "A00-B99"
    assert dx.block_description == "Certain infectious and parasitic diseases"
    assert str(dx) == "A02.1"
    assert repr(dx) == "<ICD10: A02.1>"


def test_find_neoplasm():
    dx = icd10.find("C10.1")
    assert isinstance(dx, icd10.ICD10)
    assert dx.code == "C101"
    assert dx.billable
    assert dx.description == "Malignant neoplasm of anterior surface of epiglottis"
    assert not dx.categorical
    assert dx.block == "C00-D48"
    assert dx.block_description == "Neoplasms"
    assert str(dx) == "C10.1"
    assert repr(dx) == "<ICD10: C10.1>"


def test_in_chapter():
    assert icd10.in_chapter('A00-B99', 'B20')
    assert not icd10.in_chapter('A00-B99', 'T50.B')
    assert icd10.in_chapter('H60-H95', 'H60')
    assert icd10.in_chapter('Z00-Z99', 'Z01.4')
