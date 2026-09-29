# Konsep Dasar Computer Vision

Image adalah array yang maknanya bergantung pada color space, bit depth, resolution, lens, viewpoint, illumination, dan acquisition pipeline. Resize/crop/normalization dapat mengubah sinyal; simpan transform sebagai bagian model contract.

Classification memberi label image, detection memberi object dan bounding box, segmentation memberi label per pixel, sedangkan tracking menghubungkan object lintas frame. Pilih task dari keputusan yang diperlukan, bukan dari model populer.

Data split harus memisahkan subject, asset, location, atau capture session bila mereka menciptakan korelasi. Frame video berdekatan pada train/test adalah leakage. Augmentation harus plausible secara fisik—flip tidak sah bila orientasi bermakna.

Accuracy saja tidak cukup. Gunakan confusion/error slices untuk classification, precision-recall dan IoU/mAP dengan definisi jelas untuk detection/segmentation, serta latency/memory/calibration saat deployment. Uji blur, low light, occlusion, new camera, dan out-of-distribution input. Model harus dapat abstain atau dialihkan ke review bila confidence tidak andal.
