<h1><center>Masked Sparse Adversarial Examples for Audio-Visual Speech Recognition</center></h1>

<center><b>Anonymous Author(s)</b></center>

<center>Submission Id: 1514</center> 

## Abstract
Sparse adversarial attacks design imperceptible perturbations onto partial positions of inputs that lead a neural network model to predict incorrect outputs. Until now, most researches focus on the image classification and speech recognition domain. However, research on the adversarial attack against audio-visual speech recognition is limited and faces several challenges: 1) 'dispensable regions': some audio and video regions are less important for the model in the speech recognition process. Attacking these regions brings more noise while contributes less to constructing a successful adversarial example; 2) 'sensitiveness distinction': the perceptibility of humans towards the same noise under different regions is significantly different. Particularly, perturbations are more noticeable in the periods of silences and pauses; 3) 'temporal cues': the temporal information contained in videos should be explored. In this paper, we propose a novel sparse adversarial attack scheme, MSAE, that adopts weighted masks to overcome the difficulties above. Specifically, 1) we introduce grouped selective mask to achieve grouped sparsity through backpropagation automatically; 2) the perceptibility weight matrix is introduced to ensure the imperceptibility of the audio and video respectively; 3) we utilize $l2$-norm within frames and $l1$-norm across frames to achieve spatial and temporal sparsity. Experiments on the LRS2-BBC dataset demonstrate the effectiveness of MSAE: it achieves the lowest noise level among several state-of-the-art attack baselines even when only a portion of the input is perturbed. Moreover, our work is the first attempt to implement a successful sparse attack against the audio-visual speech recognition systems.

## Audio/Video Adversarial Examples
*Note: All samples are in LRS2-BBC dataset[1].*

### 1. Audio Adversarial Examples

<div>
	<audio src="MSAE_FPM/BUT BEFORE I DO.wav" controls="controls" style='display:inline-block;'>
	Your browser does not support the audio element.
	</audio>
	<label for="audio1" style='display:inline-block;line-height:54px;font-size:24px;font-weight:bold;'>[Reveal Transcription]</label>
	<input id="audio1" type="submit" value="在线支付" onclick="display('lb')" style="display:none">
	<div id="lb" style="display:none">
		<strong>Clean audio:</strong> “But before I do.”
	</div>
</div>

### 2. Video Adversarial Examples

<video src="MSAE_FPM/BUT BEFORE I DO.mp4" controls="controls">
  Your browser does not support the HTML5 video element.
</video>

<video src="MSAE_FPM/IF IT WAS GOING TO BE INCREASED.mp4" controls="controls">
  Your browser does not support the HTML5 video element.
</video>


## References
[1] Afouras T, Chung J S, Senior A, et al. Deep audio-visual speech recognition[J]. IEEE transactions on pattern analysis and machine intelligence, 2018.




<script type="text/javascript">
 
    function display(id){  
        var traget=document.getElementById(id);  
        if(traget.style.display=="none"){  
            traget.style.display="";  
        }else{  
            traget.style.display="none";  
      }  
   }  
</script>
