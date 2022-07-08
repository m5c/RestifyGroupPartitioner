import FileInterpreter
import MarkDownPrinter
from distributor.ScoreBasedDistributor import ScoreBasedDistributor
from distributor.MinniMaxOptimizer import optimize

# Main script logic
FileInterpreter.verify_input_files()
participants = FileInterpreter.extract_participants()

# If you are not interested in building control groups and only want to see the overall stats, just comment out the
# next line and change the MarkDownPrinter command to the one commented out.
partition = ScoreBasedDistributor(participants, ['Red', 'Green', 'Blue', 'Yellow']).partition()
partition = optimize(partition)
MarkDownPrinter.build_markdown_with_partition(participants, partition)
#MarkDownPrinter.build_markdown(participants)
print("Open this file in your browser: ///tmp/recruitment.md")
