import SelfScoreFileParser
import MarkDownPrinter
from distributor.ScoreBasedDistributor import ScoreBasedDistributor
from distributor.MinniMaxOptimizer import optimize_once, optimize

# Main script logic
from invitationgen.MetaBundleFiller import parse_all_emails, complete_with_partition_info
from invitationgen.UploadUrlFileParser import parse_all_upload_locations

## Generate partitions with originals
SelfScoreFileParser.verify_input_files()
participants = SelfScoreFileParser.extract_participants()
partition = ScoreBasedDistributor(participants, ['Red', 'Green', 'Blue', 'Yellow']).partition()
partition = optimize(partition)

## Remove dropped out by code names and test all permutations with backup personnel
droppers = ["red-zebra", "green-raccoon", "red-raccoon", "yellow-squid", "blue-koala"]
backup_participants = SelfScoreFileParser.extract_backup_participants()
reduced_partition = remove_droppers(partition, droppers)

## Generate spreadhsheet and links
upload_locations = parse_all_upload_locations()
meta_bundles = parse_all_emails()
meta_bundles = complete_with_partition_info(meta_bundles, partition, upload_locations)
MarkDownPrinter.build_markdown_with_partition(participants, partition, meta_bundles)
print("Open this file in your browser: ///tmp/recruitment.md")
