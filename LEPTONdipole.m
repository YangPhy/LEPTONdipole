(* ::Package:: *)
(* ************************************************************************* *)
(*         FeynRules script for LEPTONdipole model                           *)
(* ************************************************************************* *)

currentDir = DirectoryName[$InputFileName];
If[currentDir === "" || !StringQ[currentDir],
  currentDir = Directory[];
];
SetDirectory[currentDir];

$FeynRulesPath = ExpandFileName[FileNameJoin[{currentDir, "..", ".."}]];
If[!MemberQ[$Path, $FeynRulesPath], PrependTo[$Path, $FeynRulesPath]];

If[!ValueQ[target] || !StringQ[target],
  target = "UFO_Unitary";
];

Print["========================================================"];
Print["[LEPTONdipole] Target:            ", target];
Print["[LEPTONdipole] Working Directory: ", currentDir];
Print["[LEPTONdipole] FeynRules Path:    ", $FeynRulesPath];
Print["========================================================"];

<< FeynRules`;
SetDirectory[currentDir];

FR$DSign = -1;

Switch[target,
  "FA_Unitary",
    FeynmanGauge = False;
    LoadModel["SM.fr", "LEPTONdipole.fr"];
    FeynmanGauge = False;
    LTotal = LSM + LBSM;
    WriteFeynArtsOutput[LTotal,
      FlavorExpand -> SU2W,
      Output -> "LEPTONdipole_UnitaryGauge_FA"
    ],

  "FA_Feynman",
    FeynmanGauge = True;
    LoadModel["SM.fr", "LEPTONdipole.fr"];
    FeynmanGauge = True;
    LTotal = LSM + LBSM;
    WriteFeynArtsOutput[LTotal,
      FlavorExpand -> SU2W,
      Output -> "LEPTONdipole_FeynmanGauge_FA"
    ],

  "UFO_Unitary",
    FeynmanGauge = False;
    LoadModel["SM.fr", "LEPTONdipole.fr"];
    FeynmanGauge = False;
    LTotal = LSM + LBSM;
    WriteUFO[LTotal,
      Output -> "LEPTONdipole_UnitaryGauge_UFO",
      AddDecays -> False
    ],

  "UFO_Feynman",
    FeynmanGauge = True;
    LoadModel["SM.fr", "LEPTONdipole.fr"];
    FeynmanGauge = True;
    LTotal = LSM + LBSM;
    WriteUFO[LTotal,
      Output -> "LEPTONdipole_FeynmanGauge_UFO",
      AddDecays -> False
    ],

  _,
    Print["[ERROR] Unknown target: ", target];
    Quit[1];
];

Print["\n[SUCCESS] Target ", target, " finished successfully!"];

