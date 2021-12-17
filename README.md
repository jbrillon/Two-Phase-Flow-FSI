**Date written: November 2019**

Final project for ME 506 (Two-Phase Flow and Heat Transfer) at Purdue University taught by Professor Mudawar of the Mechanical Engineering department. 

# Dynamics of pipes conveying two-phase flows

Solves the equation of motion (EoM) for pipes conveying two-phase flows using the Galerkin method; a fluid-structure interaction problem. Used to study the dynamics of the pipe, such as the response, bifurcations, and critical flow velocities, for different two-phase flow parameters. To get an overview of the study, click [here](https://drive.google.com/file/d/1LuhH4r_Lc8wFsI3muP0FPonwE33kmYJ9/view?usp=sharing) to view the presentation slides; <u>open with Adobe Acrobat</u> for animations to work. For complete details, refer to the project report by clicking [here](https://drive.google.com/file/d/1CcP_OEMLnCqMKXpf3TY-TfBXGQJkcZCj/view?usp=sharing).

## Verification

The image below represents the dynamics of vertical downflow in a cantilever pipe, reproducing literature results of <em>Paidoussis and Issid (1974)</em> for the case where the fluid is a liquid only (i.e. single phase).

<img src="https://raw.githubusercontent.com/jbrillon/Two-Phase-Flow-FSI/master/Figures/argand_pd_comparison.png" width="60%"></img>

## Restabilizing System Response

The fluid-structure system's 4th mode of excitation shows an unstable-stable-unstable response as liquid velocity is increased.

<img src="https://raw.githubusercontent.com/jbrillon/Two-Phase-Flow-FSI/master/Figures/argand_restable_a.png" width="45%"></img>
<img src="https://raw.githubusercontent.com/jbrillon/Two-Phase-Flow-FSI/master/Figures/restable/restabilization.gif" width="45%"></img>

## Unstable Transient Motion of Pipe

Flutter instability with growth at a corresponding fixed liquid velocity.

<img src="https://raw.githubusercontent.com/jbrillon/Two-Phase-Flow-FSI/master/Figures/transient_u1585.png" width="45%"></img>
<img src="https://raw.githubusercontent.com/jbrillon/Two-Phase-Flow-FSI/master/Figures/restable_spaceResponse/restable_spatial_response.gif" width="45%"></img>
