from main import *
import upload

def lambda_handler(event, context):
    credentials = load_credentials()
    session = CaesarAPI(API_PATH, credentials)
    parser = CaesarParser()
    print("Education and Courses")
    education = get_parsed_education(session, parser)
    upload.save_file("education.json", json.dumps(education))    
    print("Competences")
    competences = get_parsed_competences(session, parser)
    upload.save_file("competences.json", json.dumps(competences))
    print("Databases")
    databases = get_parsed_databases(session, parser)
    upload.save_file("databases.json", json.dumps(databases))
    print("Activities")
    activities = get_parsed_activities(session, parser)
    upload.save_file("activities.json", json.dumps(activities))
    print("Experiences")
    experiences = get_parsed_experiences(session, parser)
    upload.save_file("experiences.json", json.dumps(experiences))
    print("OS")
    os = get_parsed_os(session, parser)
    upload.save_file("os.json", json.dumps(os))
    print("Packages")
    packages = get_parsed_packages(session, parser)
    upload.save_file("packages.json", json.dumps(packages))
    print("Technologies")
    technologies = get_parsed_technologies(session, parser)
    upload.save_file("technologies.json", json.dumps(technologies))
    print("Methods")
    methods = get_parsed_methods(session, parser)
    upload.save_file("methods.json", json.dumps(methods))
    print("Development")
    development = get_parsed_development(session, parser)
    upload.save_file("development.json", json.dumps(development))
    print("Done")
