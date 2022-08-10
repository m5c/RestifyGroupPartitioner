import SelfScoreFileParser
import MarkDownPrinter
from distributor import PartitionAdjuster
from distributor.ScoreBasedDistributor import ScoreBasedDistributor
from distributor.MinniMaxOptimizer import optimize_once, optimize

# Main script logic
from invitationgen.MetaBundleFiller import parse_all_emails, complete_with_partition_info
from invitationgen.UploadUrlFileParser import parse_all_upload_locations

## Generate partitions with originals
SelfScoreFileParser.verify_input_files()
participants = SelfScoreFileParser.extract_participants("original")
partition = ScoreBasedDistributor(participants, ['Red', 'Green', 'Blue', 'Yellow']).partition()
partition = optimize(partition)

## Remove dropped out by code names and test all permutations with backup personnel
droppers = ["red-zebra", "green-raccoon", "blue-zebra", "yellow-squid", "blue-koala"]
#, "yellow-koala", "green-koala", "blue-squid"]
backup_participants = SelfScoreFileParser.extract_participants("fallback")
PartitionAdjuster.mark_droppers(partition, droppers)
PartitionAdjuster.patch_participant_list(participants, backup_participants)

## Create all permutations of backup-participant orders, find the one with best minimax value.
PartitionAdjuster.findBestBackupPermutation(partition, backup_participants)

## Replace the fallback optimized partition (targeted second generation droppers) and flip the colour blind
## Flipping means swaping the affiliated team members, updating the partition stats
PartitionAdjuster.flip("blue-zebra", "green-raccoon", partition)
## Replacing means removing a participant for good and inserting another now one from the replacers folder for good
PartitionAdjuster.singelDropperReplacer("blue-squid", 0, partition, participants)

## Generate spreadhsheet and links
upload_locations = parse_all_upload_locations()
meta_bundles = parse_all_emails()
meta_bundles = complete_with_partition_info(meta_bundles, partition, upload_locations)
MarkDownPrinter.build_markdown_with_partition(participants, partition, meta_bundles)
print("Open this file in your browser: ///tmp/recruitment.md")
