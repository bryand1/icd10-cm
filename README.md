# ICD-10 CM

![license MIT](https://s3-us-west-1.amazonaws.com/bryand1/images/badges/license-MIT-blue.svg)
![python 3.6 | 3.7](https://s3-us-west-1.amazonaws.com/bryand1/images/badges/python-3.6-3.7.svg)


ICD-10 is the 10th revision of the International Statistical Classification of Diseases and Related Health Problems (ICD),
a medical classification list by the World Health Organization (WHO). It contains codes for diseases, signs and symptoms,
abnormal findings, complaints, social circumstances, and external causes of injury or diseases.

[Wikipedia: ICD-10](https://en.wikipedia.org/wiki/ICD-10)


## Getting Started
```bash
pip install icd10-cm
```


## Common Usage

### Find an ICD-10 code
```python
import icd10

code = icd10.find("J20.0")
print(code.description)         # Acute bronchitis due to Mycoplasma pneumoniae
if code.billable:
    print(code, "is billable")  # J20.0 is billable

print(code.chapter)             # X
print(code.block)               # J00-J99
print(code.block_description)   # Diseases of the respiratory system
```

### Check if an ICD-10 code exists
```python
import icd10

if icd10.exists("J20.0"):
    print("Exists")
```


## Chapters

| Chapter | Block | Title |
| ------- | ----- | ----- |
| I | A00-B99 | Certain infectious and parasitic diseases |
| II | C00-D48 | Neoplasms |
| III | D50-D89 | Diseases of the blood and blood-forming organs and certain disorders involving the immune mechanism |
|IV | E00-E90 | Endocrine, nutritional and metabolic diseases |
| V | F00-F99 | Mental and behavioural disorders |
| VI | G00-G99 | Diseases of the nervous system |
| VII | H00-H59 | Diseases of the eye and adnexa |
| VIII | H60-H95 | Diseases of the ear and mastoid process |
| IX | I00-I99 | Diseases of the circulatory system |
| X | J00-J99 | Diseases of the respiratory system |
| XI | K00-K93 | Diseases of the digestive system |
| XII | L00-L99 | Diseases of the skin and subcutaneous tissue |
| XIII | M00-M99 | Diseases of the musculoskeletal system and connective tissue |
| XIV | N00-N99 | Diseases of the genitourinary system |
| XV | O00-O99 | Pregnancy, childbirth and the puerperium |
| XVI | P00-P96 | Certain conditions originating in the perinatal period |
| XVII | Q00-Q99 | Congenital malformations, deformations and chromosomal abnormalities |
| XVIII | R00-R99 | Symptoms, signs and abnormal clinical and laboratory findings, not elsewhere classified |
| XIX | S00-T98 | Injury, poisoning and certain other consequences of external causes |
| XX | V01-Y98 | External causes of morbidity and mortality |
| XXI | Z00-Z99 | Factors influencing health status and contact with health services |
| XXII | U00-U99 | Codes for special purposes |

[Wikipedia: ICD-10](https://en.wikipedia.org/wiki/ICD-10#List)
