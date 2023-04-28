class ReadMe:
    def __init__(self):
        self.username = input("Enter your username: ")
        self.contacts = {
            "Email": input("Enter your email address: "),
            "Discord": input("Enter your Discord username and tag: ")
        }
        self.aliases = input("Enter any aliases you go by, separated by commas: ").split(",")
        self.occupation = input("Enter your occupation: ")
        self.skills = input("Enter your skills, separated by commas: ").split(",")
        self.projects = []
        num_projects = int(input("How many projects would you like to include? "))
        for i in range(num_projects):
            project_name = input("Enter the name of project " + str(i+1) + ": ")
            project_desc = input("Enter a brief description of project " + str(i+1) + ": ")
            project_link = input("Enter the link to project " + str(i+1) + ": ")
            self.projects.append({
                "name": project_name,
                "description": project_desc,
                "link": project_link
            })
        self.hobbies = input("Enter your hobbies, separated by commas: ").split(",")

    def generate(self):
        readme = f"# {self.username}\n\n"
        readme += "## Contacts\n"
        for contact in self.contacts:
            readme += f"- {contact}: {self.contacts[contact]}\n"
        readme += "\n"
        readme += "## Aliases\n"
        for alias in self.aliases:
            readme += f"- {alias}\n"
        readme += "\n"
        readme += f"## Occupation\n{self.occupation}\n\n"
        readme += "## Skills\n"
        for skill in self.skills:
            readme += f"- {skill}\n"
        readme += "\n"
        readme += "## Projects\n"
        for project in self.projects:
            readme += f"- [{project['name']}]({project['link']}): {project['description']}\n"
        readme += "\n"
        readme += "## Hobbies\n"
        for hobby in self.hobbies:
            readme += f"- {hobby}\n"
        return readme
