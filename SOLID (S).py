class Report:
    def __init__(self, title, content):
        self.title = title
        self.content = content
class Work_to_PDF:
    def generate_pdf(self):
        print("PDF generated")

class Operation_to_file:
    def save_to_file(self, filename):
        print(f"Saved {filename}")