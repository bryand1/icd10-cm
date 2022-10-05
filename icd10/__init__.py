"""
ICD-10 CM

ICD-10 is the 10th revision of the International Statistical Classification of Diseases and
Related Health Problems (ICD), a medical classification list by the World Health Organization (WHO).
It contains codes for diseases, signs and symptoms, abnormal findings, complaints, social circumstances,
and external causes of injury or diseases.
"""
import gzip
import json
import os
from typing import Optional

here = os.path.dirname(os.path.abspath(__file__))
with gzip.open(os.path.join(here, 'icd10.json.gz')) as fh:
    codes = json.load(fh)

# https://en.wikipedia.org/wiki/ICD-10#List
chapters = [
    ('I', 'A00-B99', 'Certain infectious and parasitic diseases'),
    ('II', 'C00-D48', 'Neoplasms'),
    ('III', 'D50-D89', 'Diseases of the blood and blood-forming organs and certain disorders involving the immune mechanism'),
    ('IV', 'E00-E90', 'Endocrine, nutritional and metabolic diseases'),
    ('V', 'F00-F99', 'Mental and behavioural disorders'),
    ('VI', 'G00-G99', 'Diseases of the nervous system'),
    ('VII', 'H00-H59', 'Diseases of the eye and adnexia'),
    ('VIII', 'H60-H95', 'Diseases of the ear and mastoid process'),
    ('IX', 'I00-I99', 'Diseases of the circulatory system'),
    ('X', 'J00-J99', 'Diseases of the respiratory system'),
    ('XI', 'K00-K93', 'Diseases of the digestive system'),
    ('XII', 'L00-L99', 'Diseases of the skin and subcutaneous tissue'),
    ('XIII', 'M00-M99', 'Diseases of the musculoskeletal system and connective tissue'),
    ('XIV', 'N00-N99', 'Diseases of the genitourinary system'),
    ('XV', 'O00-O99', 'Pregnancy, childbirth and the puerperium'),
    ('XVI', 'P00-P96', 'Certain conditions originating in the perinatal period'),
    ('XVII', 'Q00-Q99', 'Congenital malformations, deformations and chromosomal abnormalities'),
    ('XVIII', 'R00-R99', 'Symptoms, signs and abnormal clinical and laboratory findings, not elsewhere classified'),
    ('XIX', 'S00-T98', 'Injury, poisoning and certain other consequences of external causes'),
    ('XX', 'V01-Y98', 'External causes of morbidity and mortality'),
    ('XXI', 'Z00-Z99', 'Factors influencing health status and contact with health services'),
    ('XXII', 'U00-U99', 'Codes for special purposes'),
]


class ICD10:

    def __init__(self, code: str, billable: bool, description: str):
        self.code = code
        self.billable = billable
        self.categorical = not billable
        self.description = description
        self._chapter = None
        self._block = None
        self._block_description = None

    @property
    def chapter(self) -> str:
        if self._chapter is not None:
            return self._chapter
        self._find_chapter()
        return self._chapter

    @property
    def block(self) -> str:
        if self._block is not None:
            return self._block
        self._find_chapter()
        return self._block

    @property
    def block_description(self) -> str:
        if self._block_description is not None:
            return self._block_description
        self._find_chapter()
        return self._block_description

    def __str__(self):
        if len(self.code) > 3:
            return self.code[:3] + '.' + self.code[3:]
        else:
            return self.code

    def __repr__(self):
        return "<ICD10: %s>" % self

    def __hash__(self):
        return hash(self.code)

    def _find_chapter(self):
        for chapter, block, description in chapters:
            if in_chapter(block, self.code):
                self._chapter = chapter
                self._block = block
                self._block_description = description
                break


def exists(s: str) -> bool:
    """
    >>> exists("T50.B")
    True
    >>> exists("A99.8")
    False
    """
    if not s:
        return False
    return bool(codes.get(s.replace('.', ''), False))


def find(s: str) -> Optional[ICD10]:
    """
    >>> find("A02.1")
    <ICD10: A02.1>
    """
    if not s:
        return
    k = s.replace('.', '')
    v = codes.get(k)
    if v is None:
        return
    billable, description = v
    return ICD10(k, billable, description)


def in_chapter(block: str, icd10: str) -> bool:
    alpha, numeric = ord(icd10[0]), int(icd10[1:3].lstrip('0'))
    sblock, eblock = block.split('-')  # A00-B99
    salpha, snumeric = ord(sblock[0]), int(sblock[1:].lstrip('0') or 0)
    ealpha, enumeric = ord(eblock[0]), int(eblock[1:].lstrip('0') or 0)
    return salpha <= alpha <= ealpha and snumeric <= numeric <= enumeric
