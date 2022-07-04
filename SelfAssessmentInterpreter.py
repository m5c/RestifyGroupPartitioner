from MarkDownPrinter import build_markdown
import FileInterpreter
import MarkDownPrinter


# Main script logic
FileInterpreter.verify_input_files()
participants = FileInterpreter.extract_participants()
MarkDownPrinter.build_markdown(participants)
print("Open this file in your browser: ///tmp/recruitment.md")
