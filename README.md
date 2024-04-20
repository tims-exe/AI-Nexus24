Progress Summary:


•	Investigated the diverse vocal repertoires of target species, including whistles, barks, and pulsed calls. Identified the importance of linking specific call types to behaviors for model development.

•	Evaluated the potential of VGGish, a pre-trained audio feature extraction model. Acknowledged limitations of VGGish's generic audio focus and the need for further exploration in translating features to specific calls.

•	Highlighted the need for custom model development with feature engineering techniques like Mel-frequency cepstral coefficients (MFCCs) and time-domain features. Emphasized building a multi-class classification model for various vocalization types.

•	Identified data scarcity and the critical role of well-labeled datasets with specific call types.

•	Suggested exploring transfer learning with pre-trained audio classification models potentially better suited for bioacoustic tasks. Decided to fine-tune the model on a custom dataset.

•	Proposed training separate models for different target species (if resources allow) for potentially improved accuracy.

•	Investigate existing underwater acoustic datasets containing marine mammal vocalizations relevant to the target region.

•	Research feature engineering techniques specifically designed for marine mammal call classification.

•	Exploring ways to load custom dataset to the VGGish model. (Current hurdle to tackle aka learning phase :D  TIMESTAMP-16:05)

• Training dataset found. Lack of behavioral vocalization but identification possible.

• Processed audio data and conversion to spectogram successfull. Need to process the entire data.

• Figuring out to load the processed dataset to train the model. (TIMESTAMP-18:45)



