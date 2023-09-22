from owlready2 import get_ontology
from alive_progress import alive_bar
from cdc_ctt.util.config import Configuration
from cdc_ctt.graph.individual_generator import *
from cdc_ctt.definitions.object_properties import *


class GraphGenerator:
    def __init__(self):
        self.ctt = get_ontology(Configuration.namespace)
        self.patient_generator = PatientGenerator()
        self.contact_tracing_generator = ContactTracingGenerator()
        self.interview_generator = InterviewGenerator()
        self.locating_information_generator = LocatingInformationGenerator()
        self.pre_existing_conditions_generator = PreExistingConditionsGenerator()
        self.risk_factors_generator = RiskFactorsGenerator()
        self.sars_cov2_test_generator = SARSCOV2TestGenerator()
        self.symptoms_and_clinical_course_generator = (
            SymptomsAndClinicalCourseGenerator()
        )

    def generate_one(self):
        patient = self.patient_generator.generate()
        contact_tracing = self.contact_tracing_generator.generate()
        interview = self.interview_generator.generate()
        locating_information = self.locating_information_generator.generate()
        gender = self.locating_information_generator.gender
        pre_existing_conditions = self.pre_existing_conditions_generator.generate(
            gender=gender
        )
        risk_factors = self.risk_factors_generator.generate()
        sars_cov2_test = self.sars_cov2_test_generator.generate()
        symptoms_and_clinical_course = (
            self.symptoms_and_clinical_course_generator.generate()
        )

        patient.has_contact_tracing.append(contact_tracing)
        patient.has_interview.append(interview)
        patient.has_locating_information.append(locating_information)
        patient.has_pre_existing_conditions.append(pre_existing_conditions)
        patient.has_risk_factors.append(risk_factors)
        patient.has_sars_cov2_test.append(sars_cov2_test)
        patient.has_symptoms_and_clinical_course.append(symptoms_and_clinical_course)

    def generate(self, n):
        with self.ctt:
            with alive_bar(n, title="Generating patients", bar="bubbles") as bar:
                for _ in range(n):
                    self.generate_one()
                    bar()

    def save(self, path):
        self.ctt.save(file=path, format="rdfxml")
