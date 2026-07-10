torchrun --nproc_per_node=2 train.py --model-dir models/mms-300m-ipa-doreco --dataset doreco_dataset --max-steps 8000 
./train_adapters.sh models/mms-300m-ipa-doreco doreco_dataset
torchrun --nproc_per_node=2 train.py --model-dir models/w2v2-lv-60-espeak-ipa-doreco --dataset doreco_dataset --max-steps 8000
./train_adapters.sh models/w2v2-lv-60-espeak-ipa-doreco doreco_dataset