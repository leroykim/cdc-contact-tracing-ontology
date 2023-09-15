from owlready2 import get_ontology, ObjectProperty
from cdc_ctt.util.config import Configuration
from cdc_ctt.definitions.classes import *

ctt = get_ontology(Configuration.namespace)

with ctt:

    class has_contact_tracing(ObjectProperty):
        domain = [Patient]
        range = [ContactTracing]

    class has_interview(ObjectProperty):
        domain = [Patient]
        range = [Interview]

    class has_locating_information(ObjectProperty):
        domain = [Patient]
        range = [LocatingInformation]

    class has_pre_existing_conditions(ObjectProperty):
        domain = [Patient]
        range = [PreExistingConditions]

    class has_risk_factors(ObjectProperty):
        domain = [Patient]
        range = [RiskFactors]

    class has_sars_cov2_test(ObjectProperty):
        domain = [Patient]
        range = [SARSCOV2Test]

    class has_symptoms_and_clinical_course(ObjectProperty):
        domain = [Patient]
        range = [SymptomsAndClinicalCourse]
