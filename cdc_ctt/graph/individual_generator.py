from abc import ABC, abstractmethod
import datetime
from faker import Faker
import random
import uuid

from cdc_ctt.util.config import Configuration
from cdc_ctt.definitions.classes import *
from cdc_ctt.definitions.data_properties import *


class IndividualGenerator(ABC):
    def __init__(self):
        self.start_date = datetime.datetime.strptime(
            Configuration.start_date, Configuration.date_format
        ).date()
        self.end_date = datetime.datetime.strptime(
            Configuration.end_date, Configuration.date_format
        ).date()

    @abstractmethod
    def generate(self):
        pass

    def get_random_date(self) -> datetime.date:
        delta = self.end_date - self.start_date
        random_number_of_days = random.randint(0, delta.days)
        random_date = self.start_date + datetime.timedelta(days=random_number_of_days)
        return random_date

    def get_random_datetime_after(self, after: datetime.date) -> datetime.date:
        delta = self.end_date - after
        random_number_of_days = random.randint(0, delta.days)
        random_date = after + datetime.timedelta(days=random_number_of_days)
        return random_date


class PatientGenerator(IndividualGenerator):
    def __init__(self):
        super().__init__()

    def generate(self):
        patient = Patient()
        patient.date_assigned_to_investigation.append(self.get_random_date())
        patient.patient_id.append(str(uuid.uuid4()))
        return patient


class ContactTracingGenerator(IndividualGenerator):
    def __init__(self):
        super().__init__()

    def generate(self):
        contact_tracing = ContactTracing()
        household_contact = random.choice(Configuration.YNUR)
        contact_tracing.any_household_contact.append(household_contact)
        if household_contact == "Y":
            contact_tracing.total_number_of_household_contacts.append(
                random.randint(0, 10)
            )
        else:
            contact_tracing.total_number_of_household_contacts.append(0)
        contact_tracing.can_self_isolate.append(random.choice(Configuration.YNUR))
        contact_tracing.need_assistance_to_self_isolate.append(
            random.choice(Configuration.YNUR)
        )
        intimate_partners = random.choice(Configuration.YNUR)
        contact_tracing.any_intimate_partners.append(intimate_partners)
        if intimate_partners == "Y":
            contact_tracing.total_number_of_intimate_partners.append(
                random.randint(0, 10)
            )
        else:
            contact_tracing.total_number_of_intimate_partners.append(0)
        contact_tracing.any_other_close_contact.append(
            random.choice(Configuration.YNUR)
        )
        return contact_tracing


class InterviewGenerator(IndividualGenerator):
    def __init__(self):
        super().__init__()

    def generate(self):
        interview = Interview()
        interview.interview_1_occurred.append(random.choice(Configuration.YNPR))
        interview.interview_2_occurred.append(random.choice(Configuration.YNPR))
        interview.interview_3_occurred.append(random.choice(Configuration.YNPR))
        interview.date_of_interview_attempt_1.append(self.get_random_date())
        interview.date_of_interview_attempt_2.append(self.get_random_date())
        interview.date_of_interview_attempt_3.append(self.get_random_date())

        return interview


class LocatingInformationGenerator(IndividualGenerator):
    def __init__(self):
        super().__init__()
        self.fake = Faker("en_US")
        self.gender = None

    def generate(self):
        locating_information = LocatingInformation()
        locating_information.born_in_the_united_states.append(
            random.choice(Configuration.YNUR)
        )
        locating_information.city_of_residence.append(self.fake.city())
        locating_information.dob.append(self.fake.date_of_birth())
        locating_information.email_1.append(self.fake.free_email())
        locating_information.email_2.append(self.fake.company_email())
        locating_information.ethnicity.append(random.choice(Configuration.ETHNICITY))
        locating_information.first_name.append(self.fake.first_name())
        locating_information.last_name.append(self.fake.last_name())
        gender = random.choice(Configuration.GENDER)
        locating_information.gender.append(gender)
        locating_information.interpreter_used.append(random.choice(Configuration.YNUR))
        locating_information.ok_to_email.append(random.choice(Configuration.YNUR))
        locating_information.ok_to_text.append(random.choice(Configuration.YNPR))
        locating_information.phone_number_1.append(self.fake.phone_number())
        locating_information.phone_number_2.append(self.fake.phone_number())
        locating_information.primary_language.append(
            random.choice(Configuration.LANGUAGE)
        )
        locating_information.race.append(random.choice(Configuration.RACE))
        locating_information.residential_street_address.append(
            self.fake.street_address()
        )
        locating_information.state_of_residence.append(self.fake.state_abbr())
        locating_information.zip_code.append(self.fake.zipcode_in_state())

        self.gender = gender
        return locating_information


class PreExistingConditionsGenerator(IndividualGenerator):
    def __init__(self):
        super().__init__()

    def generate(self, gender):
        pre_existing_conditions = PreExistingConditions()
        pre_existing_conditions.chronic_liver_disease.append(
            random.choice(Configuration.YNPR)
        )
        pre_existing_conditions.chronic_lung_disease.append(
            random.choice(Configuration.YNPR)
        )
        pre_existing_conditions.chronic_renal_disease.append(
            random.choice(Configuration.YNPR)
        )
        pre_existing_conditions.cvd.append(random.choice(Configuration.YNPR))
        pre_existing_conditions.diabetes.append(random.choice(Configuration.YNPR))
        pre_existing_conditions.immunocompromised.append(
            random.choice(Configuration.YNPR)
        )
        if gender == "F":
            pre_existing_conditions.pregnant.append(random.choice(Configuration.YNPR))
        else:
            pre_existing_conditions.pregnant.append("N")
        pre_existing_conditions.severe_obesity.append(random.choice(Configuration.YNPR))

        return pre_existing_conditions


class RiskFactorsGenerator(IndividualGenerator):
    def __init__(self):
        super().__init__()

    def generate(self):
        risk_factors = RiskFactors()
        congregate = random.choice(Configuration.YNUR)
        risk_factors.congregate.append(congregate)
        if congregate == "Y":
            risk_factors.congregate_setting.append(
                random.choice(Configuration.CONGREGATE)
            )
        risk_factors.contact_with_confirmed_covid_case.append(
            random.choice(Configuration.YNUR)
        )
        risk_factors.employed.append(random.choice(Configuration.EMPLOYED))
        hcp = random.choice(Configuration.YNUR)
        risk_factors.hcp.append(hcp)
        if hcp == "Y":
            risk_factors.hcp_setting.append(random.choice(Configuration.HCP))
        return risk_factors


class SARSCOV2TestGenerator(IndividualGenerator):
    def __init__(self):
        super().__init__()

    def generate(self):
        sars_cov2_test = SARSCOV2Test()
        sars_cov2_test_occurred = random.choice(Configuration.YNUR)
        sars_cov2_test.sars_cov2_test_occurred.append(sars_cov2_test_occurred)
        if sars_cov2_test_occurred == "Y":
            first_sars_cov2_test_date = self.get_random_date()
            last_sars_cov2_test_date = self.get_random_datetime_after(
                first_sars_cov2_test_date
            )
            sars_cov2_test.date_of_first_sars_cov2_test.append(
                first_sars_cov2_test_date
            )
            sars_cov2_test.date_of_last_sars_cov2_test.append(last_sars_cov2_test_date)
            sars_cov2_test.result_of_first_sars_cov2_test.append(
                random.choice(Configuration.PNUE)
            )
            sars_cov2_test.result_of_last_sars_cov2_test.append(
                random.choice(Configuration.PNUE)
            )
        return sars_cov2_test


class SymptomsAndClinicalCourseGenerator(IndividualGenerator):
    def __init__(self):
        super().__init__()

    def generate(self):
        symptoms_and_clinical_course = SymptomsAndClinicalCourse()
        symptoms_and_clinical_course.abdominal_pain.append(
            random.choice(Configuration.YNUR)
        )
        symptoms_and_clinical_course.chills.append(random.choice(Configuration.YNUR))
        symptoms_and_clinical_course.cough.append(random.choice(Configuration.YNUR))
        symptoms_and_clinical_course.death.append(random.choice(Configuration.YNPR))
        symptoms_and_clinical_course.diarrhea_gi.append(
            random.choice(Configuration.YNUR)
        )
        symptoms_and_clinical_course.ecmo.append(random.choice(Configuration.YNPR))
        symptoms_and_clinical_course.fatigue.append(random.choice(Configuration.YNUR))
        symptoms_and_clinical_course.fever.append(random.choice(Configuration.YNUR))
        symptoms_and_clinical_course.headache.append(random.choice(Configuration.YNUR))
        symptoms_and_clinical_course.hospitalized.append(
            random.choice(Configuration.YNPR)
        )
        symptoms_and_clinical_course.icu.append(random.choice(Configuration.YNPR))
        symptoms_and_clinical_course.loss_of_sense_of_smell.append(
            random.choice(Configuration.YNUR)
        )
        symptoms_and_clinical_course.loss_of_sense_of_taste.append(
            random.choice(Configuration.YNUR)
        )
        symptoms_and_clinical_course.malaise.append(random.choice(Configuration.YNUR))
        symptoms_and_clinical_course.mi.append(random.choice(Configuration.YNPR))
        symptoms_and_clinical_course.muscle_ache.append(
            random.choice(Configuration.YNUR)
        )
        symptoms_and_clinical_course.nasal_congestion.append(
            random.choice(Configuration.YNUR)
        )
        symptoms_and_clinical_course.pneumonia.append(random.choice(Configuration.YNUR))
        symptoms_and_clinical_course.shortness_of_breath.append(
            random.choice(Configuration.YNUR)
        )
        symptoms_and_clinical_course.sore_throat.append(
            random.choice(Configuration.YNUR)
        )
        symptoms_and_clinical_course.stroke.append(random.choice(Configuration.YNPR))
        symptoms_and_clinical_course.vomiting.append(random.choice(Configuration.YNUR))
        symptoms_and_clinical_course.date_of_symptom_onset.append(
            self.get_random_date()
        )

        return symptoms_and_clinical_course
