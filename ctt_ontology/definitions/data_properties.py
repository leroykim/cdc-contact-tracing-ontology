import datetime
from owlready2 import get_ontology, DataProperty
from ctt_ontology.util.config import Configuration
from ctt_ontology.definitions.classes import *

ctt = get_ontology(Configuration.namespace)

with ctt:
    # Patient data properties
    class date_assigned_to_investigation(DataProperty):
        domain = [Patient]
        range = [datetime.date]

    class patient_id(DataProperty):
        domain = [Patient]
        range = [str]

    # ContactTracing data properties
    class any_household_contact(DataProperty):
        domain = [ContactTracing]
        range = [str]

    class total_number_of_household_contacts(DataProperty):
        domain = [ContactTracing]
        range = [int]

    class can_self_isolate(DataProperty):
        domain = [ContactTracing]
        range = [str]

    class need_assistance_to_self_isolate(DataProperty):
        domain = [ContactTracing]
        range = [str]

    class any_intimate_partners(DataProperty):
        domain = [ContactTracing]
        range = [str]

    class total_number_of_intimate_partners(DataProperty):
        domain = [ContactTracing]
        range = [int]

    class any_other_close_contact(DataProperty):
        domain = [ContactTracing]
        range = [str]

    # Interview data properties
    class interview_1_occurred(DataProperty):
        domain = [Interview]
        range = [str]

    class interview_2_occurred(DataProperty):
        domain = [Interview]
        range = [str]

    class interview_3_occurred(DataProperty):
        domain = [Interview]
        range = [str]

    class date_of_interview_attempt_1(DataProperty):
        domain = [Interview]
        range = [datetime.date]

    class date_of_interview_attempt_2(DataProperty):
        domain = [Interview]
        range = [datetime.date]

    class date_of_interview_attempt_3(DataProperty):
        domain = [Interview]
        range = [datetime.date]

    # LocatingInformation data properties
    class born_in_the_united_states(DataProperty):
        domain = [LocatingInformation]
        range = [str]

    class city_of_residence(DataProperty):
        domain = [LocatingInformation]
        range = [str]

    class dob(DataProperty):
        domain = [LocatingInformation]
        range = [datetime.date]

    class email_1(DataProperty):
        domain = [LocatingInformation]
        range = [str]

    class email_2(DataProperty):
        domain = [LocatingInformation]
        range = [str]

    class ethnicity(DataProperty):
        domain = [LocatingInformation]
        range = [str]

    class first_name(DataProperty):
        domain = [LocatingInformation]
        range = [str]

    class last_name(DataProperty):
        domain = [LocatingInformation]
        range = [str]

    class gender(DataProperty):
        domain = [LocatingInformation]
        range = [str]

    class interpreter_used(DataProperty):
        domain = [LocatingInformation]
        range = [str]

    class ok_to_email(DataProperty):
        domain = [LocatingInformation]
        range = [str]

    class ok_to_text(DataProperty):
        domain = [LocatingInformation]
        range = [str]

    class phone_number_1(DataProperty):
        domain = [LocatingInformation]
        range = [str]

    class phone_number_2(DataProperty):
        domain = [LocatingInformation]
        range = [str]

    class primary_language(DataProperty):
        domain = [LocatingInformation]
        range = [str]

    class race(DataProperty):
        domain = [LocatingInformation]
        range = [str]

    class residential_street_address(DataProperty):
        domain = [LocatingInformation]
        range = [str]

    class state_of_residence(DataProperty):
        domain = [LocatingInformation]
        range = [str]

    class zip_code(DataProperty):
        domain = [LocatingInformation]
        range = [int]

    # PreExistingConditions data properties
    class chronic_liver_disease(DataProperty):
        domain = [PreExistingConditions]
        range = [str]

    class chronic_lung_disease(DataProperty):
        domain = [PreExistingConditions]
        range = [str]

    class chronic_renal_disease(DataProperty):
        domain = [PreExistingConditions]
        range = [str]

    class cvd(DataProperty):
        domain = [PreExistingConditions]
        range = [str]

    class diabetes(DataProperty):
        domain = [PreExistingConditions]
        range = [str]

    class immunocompromised(DataProperty):
        domain = [PreExistingConditions]
        range = [str]

    class pregnant(DataProperty):
        domain = [PreExistingConditions]
        range = [str]

    class severe_obesity(DataProperty):
        domain = [PreExistingConditions]
        range = [str]

    # RiskFactors data properties
    class congregate(DataProperty):
        domain = [RiskFactors]
        range = [str]

    class congregate_setting(DataProperty):
        domain = [RiskFactors]
        range = [str]

    class contact_with_confirmed_covid_case(DataProperty):
        domain = [RiskFactors]
        range = [str]

    class employed(DataProperty):
        domain = [RiskFactors]
        range = [str]

    class hcp(DataProperty):
        domain = [RiskFactors]
        range = [str]

    class hcp_setting(DataProperty):
        domain = [RiskFactors]
        range = [str]

    # SARSCOV2Test data properties
    class sars_cov2_test_occurred(DataProperty):
        domain = [SARSCOV2Test]
        range = [str]

    class date_of_first_sars_cov2_test(DataProperty):
        domain = [SARSCOV2Test]
        range = [datetime.date]

    class date_of_last_sars_cov2_test(DataProperty):
        domain = [SARSCOV2Test]
        range = [datetime.date]

    class result_of_first_sars_cov2_test(DataProperty):
        domain = [SARSCOV2Test]
        range = [str]

    class result_of_last_sars_cov2_test(DataProperty):
        domain = [SARSCOV2Test]
        range = [str]

    # SymptomsAndClinicalCourse data properties
    class abdominal_pain(DataProperty):
        domain = [SymptomsAndClinicalCourse]
        range = [str]

    class chills(DataProperty):
        domain = [SymptomsAndClinicalCourse]
        range = [str]

    class cough(DataProperty):
        domain = [SymptomsAndClinicalCourse]
        range = [str]

    class death(DataProperty):
        domain = [SymptomsAndClinicalCourse]
        range = [str]

    class diarrhea_gi(DataProperty):
        domain = [SymptomsAndClinicalCourse]
        range = [str]

    class ecmo(DataProperty):
        domain = [SymptomsAndClinicalCourse]
        range = [str]

    class fatigue(DataProperty):
        domain = [SymptomsAndClinicalCourse]
        range = [str]

    class fever(DataProperty):
        domain = [SymptomsAndClinicalCourse]
        range = [str]

    class headache(DataProperty):
        domain = [SymptomsAndClinicalCourse]
        range = [str]

    class hospitalized(DataProperty):
        domain = [SymptomsAndClinicalCourse]
        range = [str]

    class icu(DataProperty):
        domain = [SymptomsAndClinicalCourse]
        range = [str]

    class loss_of_sense_of_smell(DataProperty):
        domain = [SymptomsAndClinicalCourse]
        range = [str]

    class loss_of_sense_of_taste(DataProperty):
        domain = [SymptomsAndClinicalCourse]
        range = [str]

    class malaise(DataProperty):
        domain = [SymptomsAndClinicalCourse]
        range = [str]

    class mi(DataProperty):
        domain = [SymptomsAndClinicalCourse]
        range = [str]

    class muscle_ache(DataProperty):
        domain = [SymptomsAndClinicalCourse]
        range = [str]

    class nasal_congestion(DataProperty):
        domain = [SymptomsAndClinicalCourse]
        range = [str]

    class pneumonia(DataProperty):
        domain = [SymptomsAndClinicalCourse]
        range = [str]

    class shortness_of_breath(DataProperty):
        domain = [SymptomsAndClinicalCourse]
        range = [str]

    class sore_throat(DataProperty):
        domain = [SymptomsAndClinicalCourse]
        range = [str]

    class stroke(DataProperty):
        domain = [SymptomsAndClinicalCourse]
        range = [str]

    class vomiting(DataProperty):
        domain = [SymptomsAndClinicalCourse]
        range = [str]

    class date_of_symptom_onset(DataProperty):
        domain = [SymptomsAndClinicalCourse]
        range = [datetime.date]
