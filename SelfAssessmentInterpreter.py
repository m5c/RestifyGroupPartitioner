import SelfScoreFileParser
import MarkDownPrinter
from distributor.ScoreBasedDistributor import ScoreBasedDistributor
from distributor.MinniMaxOptimizer import optimize_once, optimize

# Main script logic
from invitationgen.MetaBundleFiller import parse_all_emails, complete_with_partition_info
from invitationgen.UploadUrlFileParser import parse_all_upload_locations

SelfScoreFileParser.verify_input_files()
participants = SelfScoreFileParser.extract_participants()
partition = ScoreBasedDistributor(participants, ['Red', 'Green', 'Blue', 'Yellow']).partition()
partition = optimize(partition)

upload_locations = parse_all_upload_locations()
meta_bundles = parse_all_emails()
meta_bundles = complete_with_partition_info(meta_bundles, partition, upload_locations)
MarkDownPrinter.build_markdown_with_partition(participants, partition, meta_bundles)
print("Open this file in your browser: ///tmp/recruitment.md")
