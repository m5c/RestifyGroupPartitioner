from MarkDownPrinter import build_markdown
import FileInterpreter
import MarkDownPrinter
from ScoreBasedDistributor import ScoreBasedDistributor

# Main script logic
FileInterpreter.verify_input_files()
participants = FileInterpreter.extract_participants()
control_groups = ScoreBasedDistributor(participants, ['Red', 'Green', 'Blue', 'Yellow']).partition()
MarkDownPrinter.build_markdown(participants, control_groups)
print("Open this file in your browser: ///tmp/recruitment.md")
