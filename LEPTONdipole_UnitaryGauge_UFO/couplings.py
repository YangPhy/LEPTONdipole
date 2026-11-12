# This file was automatically created by FeynRules 2.3.49
# Mathematica version: 13.1.0 for Mac OS X ARM (64-bit) (June 16, 2022)
# Date: Thu 12 Nov 2026 23:11:38


from object_library import all_couplings, Coupling

from function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot



GC_1 = Coupling(name = 'GC_1',
                value = '(ee*complex(0,1))/3.',
                order = {'QED':1})

GC_2 = Coupling(name = 'GC_2',
                value = '(-2*ee*complex(0,1))/3.',
                order = {'QED':1})

GC_3 = Coupling(name = 'GC_3',
                value = '-(ee*complex(0,1))',
                order = {'QED':1})

GC_4 = Coupling(name = 'GC_4',
                value = 'ee*complex(0,1)',
                order = {'QED':1})

GC_5 = Coupling(name = 'GC_5',
                value = 'ee**2*complex(0,1)',
                order = {'QED':2})

GC_6 = Coupling(name = 'GC_6',
                value = '-(complex(0,1)*G)',
                order = {'QCD':1})

GC_7 = Coupling(name = 'GC_7',
                value = 'G',
                order = {'QCD':1})

GC_8 = Coupling(name = 'GC_8',
                value = 'complex(0,1)*G**2',
                order = {'QCD':2})

GC_9 = Coupling(name = 'GC_9',
                value = '-6*complex(0,1)*lam',
                order = {'QED':2})

GC_10 = Coupling(name = 'GC_10',
                 value = '-(CeWIm/LambdaEFT**2)',
                 order = {'NP':1,'NPCeW':1,'NPCeWIm':1,'NPIm':1,'QED':2})

GC_11 = Coupling(name = 'GC_11',
                 value = 'CeWIm/LambdaEFT**2',
                 order = {'NP':1,'NPCeW':1,'NPCeWIm':1,'NPIm':1,'QED':2})

GC_12 = Coupling(name = 'GC_12',
                 value = '(CeWRe*complex(0,1))/LambdaEFT**2',
                 order = {'NP':1,'NPCeW':1,'NPCeWRe':1,'NPRe':1,'QED':2})

GC_13 = Coupling(name = 'GC_13',
                 value = '-(CmuWIm/LambdaEFT**2)',
                 order = {'NP':1,'NPCmuW':1,'NPCmuWIm':1,'NPIm':1,'QED':2})

GC_14 = Coupling(name = 'GC_14',
                 value = 'CmuWIm/LambdaEFT**2',
                 order = {'NP':1,'NPCmuW':1,'NPCmuWIm':1,'NPIm':1,'QED':2})

GC_15 = Coupling(name = 'GC_15',
                 value = '(CmuWRe*complex(0,1))/LambdaEFT**2',
                 order = {'NP':1,'NPCmuW':1,'NPCmuWRe':1,'NPRe':1,'QED':2})

GC_16 = Coupling(name = 'GC_16',
                 value = '-(CtaWIm/LambdaEFT**2)',
                 order = {'NP':1,'NPCtaW':1,'NPCtaWIm':1,'NPIm':1,'QED':2})

GC_17 = Coupling(name = 'GC_17',
                 value = 'CtaWIm/LambdaEFT**2',
                 order = {'NP':1,'NPCtaW':1,'NPCtaWIm':1,'NPIm':1,'QED':2})

GC_18 = Coupling(name = 'GC_18',
                 value = '(CtaWRe*complex(0,1))/LambdaEFT**2',
                 order = {'NP':1,'NPCtaW':1,'NPCtaWRe':1,'NPRe':1,'QED':2})

GC_19 = Coupling(name = 'GC_19',
                 value = '(CeBIm*cw)/(LambdaEFT**2*cmath.sqrt(2))',
                 order = {'NP':1,'NPCeB':1,'NPCeBIm':1,'NPIm':1,'QED':2})

GC_20 = Coupling(name = 'GC_20',
                 value = '(CeBRe*cw*complex(0,1))/(LambdaEFT**2*cmath.sqrt(2))',
                 order = {'NP':1,'NPCeB':1,'NPCeBRe':1,'NPRe':1,'QED':2})

GC_21 = Coupling(name = 'GC_21',
                 value = '-((CeWIm*cw)/(LambdaEFT**2*cmath.sqrt(2)))',
                 order = {'NP':1,'NPCeW':1,'NPCeWIm':1,'NPIm':1,'QED':2})

GC_22 = Coupling(name = 'GC_22',
                 value = '-((CeWRe*cw*complex(0,1))/(LambdaEFT**2*cmath.sqrt(2)))',
                 order = {'NP':1,'NPCeW':1,'NPCeWRe':1,'NPRe':1,'QED':2})

GC_23 = Coupling(name = 'GC_23',
                 value = '(CmuBIm*cw)/(LambdaEFT**2*cmath.sqrt(2))',
                 order = {'NP':1,'NPCmuB':1,'NPCmuBIm':1,'NPIm':1,'QED':2})

GC_24 = Coupling(name = 'GC_24',
                 value = '(CmuBRe*cw*complex(0,1))/(LambdaEFT**2*cmath.sqrt(2))',
                 order = {'NP':1,'NPCmuB':1,'NPCmuBRe':1,'NPRe':1,'QED':2})

GC_25 = Coupling(name = 'GC_25',
                 value = '-((CmuWIm*cw)/(LambdaEFT**2*cmath.sqrt(2)))',
                 order = {'NP':1,'NPCmuW':1,'NPCmuWIm':1,'NPIm':1,'QED':2})

GC_26 = Coupling(name = 'GC_26',
                 value = '-((CmuWRe*cw*complex(0,1))/(LambdaEFT**2*cmath.sqrt(2)))',
                 order = {'NP':1,'NPCmuW':1,'NPCmuWRe':1,'NPRe':1,'QED':2})

GC_27 = Coupling(name = 'GC_27',
                 value = '(CtaBIm*cw)/(LambdaEFT**2*cmath.sqrt(2))',
                 order = {'NP':1,'NPCtaB':1,'NPCtaBIm':1,'NPIm':1,'QED':2})

GC_28 = Coupling(name = 'GC_28',
                 value = '(CtaBRe*cw*complex(0,1))/(LambdaEFT**2*cmath.sqrt(2))',
                 order = {'NP':1,'NPCtaB':1,'NPCtaBRe':1,'NPRe':1,'QED':2})

GC_29 = Coupling(name = 'GC_29',
                 value = '-((CtaWIm*cw)/(LambdaEFT**2*cmath.sqrt(2)))',
                 order = {'NP':1,'NPCtaW':1,'NPCtaWIm':1,'NPIm':1,'QED':2})

GC_30 = Coupling(name = 'GC_30',
                 value = '-((CtaWRe*cw*complex(0,1))/(LambdaEFT**2*cmath.sqrt(2)))',
                 order = {'NP':1,'NPCtaW':1,'NPCtaWRe':1,'NPRe':1,'QED':2})

GC_31 = Coupling(name = 'GC_31',
                 value = '(CeWIm*ee)/LambdaEFT**2',
                 order = {'NP':1,'NPCeW':1,'NPCeWIm':1,'NPIm':1,'QED':3})

GC_32 = Coupling(name = 'GC_32',
                 value = '-((CeWRe*ee*complex(0,1))/LambdaEFT**2)',
                 order = {'NP':1,'NPCeW':1,'NPCeWRe':1,'NPRe':1,'QED':3})

GC_33 = Coupling(name = 'GC_33',
                 value = '(CeWRe*ee*complex(0,1))/LambdaEFT**2',
                 order = {'NP':1,'NPCeW':1,'NPCeWRe':1,'NPRe':1,'QED':3})

GC_34 = Coupling(name = 'GC_34',
                 value = '-((CmuWIm*ee)/LambdaEFT**2)',
                 order = {'NP':1,'NPCmuW':1,'NPCmuWIm':1,'NPIm':1,'QED':3})

GC_35 = Coupling(name = 'GC_35',
                 value = '(CmuWIm*ee)/LambdaEFT**2',
                 order = {'NP':1,'NPCmuW':1,'NPCmuWIm':1,'NPIm':1,'QED':3})

GC_36 = Coupling(name = 'GC_36',
                 value = '-((CmuWRe*ee*complex(0,1))/LambdaEFT**2)',
                 order = {'NP':1,'NPCmuW':1,'NPCmuWRe':1,'NPRe':1,'QED':3})

GC_37 = Coupling(name = 'GC_37',
                 value = '(CmuWRe*ee*complex(0,1))/LambdaEFT**2',
                 order = {'NP':1,'NPCmuW':1,'NPCmuWRe':1,'NPRe':1,'QED':3})

GC_38 = Coupling(name = 'GC_38',
                 value = '(CtaWIm*ee)/LambdaEFT**2',
                 order = {'NP':1,'NPCtaW':1,'NPCtaWIm':1,'NPIm':1,'QED':3})

GC_39 = Coupling(name = 'GC_39',
                 value = '-((CtaWRe*ee*complex(0,1))/LambdaEFT**2)',
                 order = {'NP':1,'NPCtaW':1,'NPCtaWRe':1,'NPRe':1,'QED':3})

GC_40 = Coupling(name = 'GC_40',
                 value = '(CtaWRe*ee*complex(0,1))/LambdaEFT**2',
                 order = {'NP':1,'NPCtaW':1,'NPCtaWRe':1,'NPRe':1,'QED':3})

GC_41 = Coupling(name = 'GC_41',
                 value = '(ee**2*complex(0,1))/(2.*sw**2)',
                 order = {'QED':2})

GC_42 = Coupling(name = 'GC_42',
                 value = '-((ee**2*complex(0,1))/sw**2)',
                 order = {'QED':2})

GC_43 = Coupling(name = 'GC_43',
                 value = '(cw**2*ee**2*complex(0,1))/sw**2',
                 order = {'QED':2})

GC_44 = Coupling(name = 'GC_44',
                 value = '-((ee*complex(0,1))/(sw*cmath.sqrt(2)))',
                 order = {'QED':1})

GC_45 = Coupling(name = 'GC_45',
                 value = '-((CKM1x1*ee*complex(0,1))/(sw*cmath.sqrt(2)))',
                 order = {'QED':1})

GC_46 = Coupling(name = 'GC_46',
                 value = '-((CKM1x2*ee*complex(0,1))/(sw*cmath.sqrt(2)))',
                 order = {'QED':1})

GC_47 = Coupling(name = 'GC_47',
                 value = '-((CKM1x3*ee*complex(0,1))/(sw*cmath.sqrt(2)))',
                 order = {'QED':1})

GC_48 = Coupling(name = 'GC_48',
                 value = '-((CKM2x1*ee*complex(0,1))/(sw*cmath.sqrt(2)))',
                 order = {'QED':1})

GC_49 = Coupling(name = 'GC_49',
                 value = '-((CKM2x2*ee*complex(0,1))/(sw*cmath.sqrt(2)))',
                 order = {'QED':1})

GC_50 = Coupling(name = 'GC_50',
                 value = '-((CKM2x3*ee*complex(0,1))/(sw*cmath.sqrt(2)))',
                 order = {'QED':1})

GC_51 = Coupling(name = 'GC_51',
                 value = '-((CKM3x1*ee*complex(0,1))/(sw*cmath.sqrt(2)))',
                 order = {'QED':1})

GC_52 = Coupling(name = 'GC_52',
                 value = '-((CKM3x2*ee*complex(0,1))/(sw*cmath.sqrt(2)))',
                 order = {'QED':1})

GC_53 = Coupling(name = 'GC_53',
                 value = '-((CKM3x3*ee*complex(0,1))/(sw*cmath.sqrt(2)))',
                 order = {'QED':1})

GC_54 = Coupling(name = 'GC_54',
                 value = '-0.5*(cw*ee*complex(0,1))/sw',
                 order = {'QED':1})

GC_55 = Coupling(name = 'GC_55',
                 value = '(cw*ee*complex(0,1))/(2.*sw)',
                 order = {'QED':1})

GC_56 = Coupling(name = 'GC_56',
                 value = '-((cw*ee*complex(0,1))/sw)',
                 order = {'QED':1})

GC_57 = Coupling(name = 'GC_57',
                 value = '(-2*cw*ee**2*complex(0,1))/sw',
                 order = {'QED':2})

GC_58 = Coupling(name = 'GC_58',
                 value = '(CeWIm*ee)/(LambdaEFT**2*sw*cmath.sqrt(2))',
                 order = {'NP':1,'NPCeW':1,'NPCeWIm':1,'NPIm':1,'QED':3})

GC_59 = Coupling(name = 'GC_59',
                 value = '(CeWRe*ee*complex(0,1))/(LambdaEFT**2*sw*cmath.sqrt(2))',
                 order = {'NP':1,'NPCeW':1,'NPCeWRe':1,'NPRe':1,'QED':3})

GC_60 = Coupling(name = 'GC_60',
                 value = '(CmuWIm*ee)/(LambdaEFT**2*sw*cmath.sqrt(2))',
                 order = {'NP':1,'NPCmuW':1,'NPCmuWIm':1,'NPIm':1,'QED':3})

GC_61 = Coupling(name = 'GC_61',
                 value = '-((CmuWRe*ee*complex(0,1))/(LambdaEFT**2*sw*cmath.sqrt(2)))',
                 order = {'NP':1,'NPCmuW':1,'NPCmuWRe':1,'NPRe':1,'QED':3})

GC_62 = Coupling(name = 'GC_62',
                 value = '(CtaWIm*ee)/(LambdaEFT**2*sw*cmath.sqrt(2))',
                 order = {'NP':1,'NPCtaW':1,'NPCtaWIm':1,'NPIm':1,'QED':3})

GC_63 = Coupling(name = 'GC_63',
                 value = '(CtaWRe*ee*complex(0,1))/(LambdaEFT**2*sw*cmath.sqrt(2))',
                 order = {'NP':1,'NPCtaW':1,'NPCtaWRe':1,'NPRe':1,'QED':3})

GC_64 = Coupling(name = 'GC_64',
                 value = '-((CeWIm*cw*ee)/(LambdaEFT**2*sw))',
                 order = {'NP':1,'NPCeW':1,'NPCeWIm':1,'NPIm':1,'QED':3})

GC_65 = Coupling(name = 'GC_65',
                 value = '-((CeWRe*cw*ee*complex(0,1))/(LambdaEFT**2*sw))',
                 order = {'NP':1,'NPCeW':1,'NPCeWRe':1,'NPRe':1,'QED':3})

GC_66 = Coupling(name = 'GC_66',
                 value = '(CeWRe*cw*ee*complex(0,1))/(LambdaEFT**2*sw)',
                 order = {'NP':1,'NPCeW':1,'NPCeWRe':1,'NPRe':1,'QED':3})

GC_67 = Coupling(name = 'GC_67',
                 value = '-((CmuWIm*cw*ee)/(LambdaEFT**2*sw))',
                 order = {'NP':1,'NPCmuW':1,'NPCmuWIm':1,'NPIm':1,'QED':3})

GC_68 = Coupling(name = 'GC_68',
                 value = '-((CmuWRe*cw*ee*complex(0,1))/(LambdaEFT**2*sw))',
                 order = {'NP':1,'NPCmuW':1,'NPCmuWRe':1,'NPRe':1,'QED':3})

GC_69 = Coupling(name = 'GC_69',
                 value = '(CmuWRe*cw*ee*complex(0,1))/(LambdaEFT**2*sw)',
                 order = {'NP':1,'NPCmuW':1,'NPCmuWRe':1,'NPRe':1,'QED':3})

GC_70 = Coupling(name = 'GC_70',
                 value = '-((CtaWIm*cw*ee)/(LambdaEFT**2*sw))',
                 order = {'NP':1,'NPCtaW':1,'NPCtaWIm':1,'NPIm':1,'QED':3})

GC_71 = Coupling(name = 'GC_71',
                 value = '-((CtaWRe*cw*ee*complex(0,1))/(LambdaEFT**2*sw))',
                 order = {'NP':1,'NPCtaW':1,'NPCtaWRe':1,'NPRe':1,'QED':3})

GC_72 = Coupling(name = 'GC_72',
                 value = '(CtaWRe*cw*ee*complex(0,1))/(LambdaEFT**2*sw)',
                 order = {'NP':1,'NPCtaW':1,'NPCtaWRe':1,'NPRe':1,'QED':3})

GC_73 = Coupling(name = 'GC_73',
                 value = '(ee*complex(0,1)*sw)/(6.*cw)',
                 order = {'QED':1})

GC_74 = Coupling(name = 'GC_74',
                 value = '-0.5*(ee*complex(0,1)*sw)/cw',
                 order = {'QED':1})

GC_75 = Coupling(name = 'GC_75',
                 value = '-((CeBIm*sw)/(LambdaEFT**2*cmath.sqrt(2)))',
                 order = {'NP':1,'NPCeB':1,'NPCeBIm':1,'NPIm':1,'QED':2})

GC_76 = Coupling(name = 'GC_76',
                 value = '-((CeBRe*complex(0,1)*sw)/(LambdaEFT**2*cmath.sqrt(2)))',
                 order = {'NP':1,'NPCeB':1,'NPCeBRe':1,'NPRe':1,'QED':2})

GC_77 = Coupling(name = 'GC_77',
                 value = '-((CeWIm*sw)/(LambdaEFT**2*cmath.sqrt(2)))',
                 order = {'NP':1,'NPCeW':1,'NPCeWIm':1,'NPIm':1,'QED':2})

GC_78 = Coupling(name = 'GC_78',
                 value = '-((CeWRe*complex(0,1)*sw)/(LambdaEFT**2*cmath.sqrt(2)))',
                 order = {'NP':1,'NPCeW':1,'NPCeWRe':1,'NPRe':1,'QED':2})

GC_79 = Coupling(name = 'GC_79',
                 value = '-((CmuBIm*sw)/(LambdaEFT**2*cmath.sqrt(2)))',
                 order = {'NP':1,'NPCmuB':1,'NPCmuBIm':1,'NPIm':1,'QED':2})

GC_80 = Coupling(name = 'GC_80',
                 value = '-((CmuBRe*complex(0,1)*sw)/(LambdaEFT**2*cmath.sqrt(2)))',
                 order = {'NP':1,'NPCmuB':1,'NPCmuBRe':1,'NPRe':1,'QED':2})

GC_81 = Coupling(name = 'GC_81',
                 value = '-((CmuWIm*sw)/(LambdaEFT**2*cmath.sqrt(2)))',
                 order = {'NP':1,'NPCmuW':1,'NPCmuWIm':1,'NPIm':1,'QED':2})

GC_82 = Coupling(name = 'GC_82',
                 value = '-((CmuWRe*complex(0,1)*sw)/(LambdaEFT**2*cmath.sqrt(2)))',
                 order = {'NP':1,'NPCmuW':1,'NPCmuWRe':1,'NPRe':1,'QED':2})

GC_83 = Coupling(name = 'GC_83',
                 value = '-((CtaBIm*sw)/(LambdaEFT**2*cmath.sqrt(2)))',
                 order = {'NP':1,'NPCtaB':1,'NPCtaBIm':1,'NPIm':1,'QED':2})

GC_84 = Coupling(name = 'GC_84',
                 value = '-((CtaBRe*complex(0,1)*sw)/(LambdaEFT**2*cmath.sqrt(2)))',
                 order = {'NP':1,'NPCtaB':1,'NPCtaBRe':1,'NPRe':1,'QED':2})

GC_85 = Coupling(name = 'GC_85',
                 value = '-((CtaWIm*sw)/(LambdaEFT**2*cmath.sqrt(2)))',
                 order = {'NP':1,'NPCtaW':1,'NPCtaWIm':1,'NPIm':1,'QED':2})

GC_86 = Coupling(name = 'GC_86',
                 value = '-((CtaWRe*complex(0,1)*sw)/(LambdaEFT**2*cmath.sqrt(2)))',
                 order = {'NP':1,'NPCtaW':1,'NPCtaWRe':1,'NPRe':1,'QED':2})

GC_87 = Coupling(name = 'GC_87',
                 value = '-0.5*(cw*ee*complex(0,1))/sw - (ee*complex(0,1)*sw)/(2.*cw)',
                 order = {'QED':1})

GC_88 = Coupling(name = 'GC_88',
                 value = 'ee**2*complex(0,1) + (cw**2*ee**2*complex(0,1))/(2.*sw**2) + (ee**2*complex(0,1)*sw**2)/(2.*cw**2)',
                 order = {'QED':2})

GC_89 = Coupling(name = 'GC_89',
                 value = '-6*complex(0,1)*lam*vev',
                 order = {'QED':1})

GC_90 = Coupling(name = 'GC_90',
                 value = '-((CeWIm*vev)/LambdaEFT**2)',
                 order = {'NP':1,'NPCeW':1,'NPCeWIm':1,'NPIm':1,'QED':1})

GC_91 = Coupling(name = 'GC_91',
                 value = '(CeWIm*vev)/LambdaEFT**2',
                 order = {'NP':1,'NPCeW':1,'NPCeWIm':1,'NPIm':1,'QED':1})

GC_92 = Coupling(name = 'GC_92',
                 value = '(CeWRe*complex(0,1)*vev)/LambdaEFT**2',
                 order = {'NP':1,'NPCeW':1,'NPCeWRe':1,'NPRe':1,'QED':1})

GC_93 = Coupling(name = 'GC_93',
                 value = '-((CmuWIm*vev)/LambdaEFT**2)',
                 order = {'NP':1,'NPCmuW':1,'NPCmuWIm':1,'NPIm':1,'QED':1})

GC_94 = Coupling(name = 'GC_94',
                 value = '(CmuWIm*vev)/LambdaEFT**2',
                 order = {'NP':1,'NPCmuW':1,'NPCmuWIm':1,'NPIm':1,'QED':1})

GC_95 = Coupling(name = 'GC_95',
                 value = '(CmuWRe*complex(0,1)*vev)/LambdaEFT**2',
                 order = {'NP':1,'NPCmuW':1,'NPCmuWRe':1,'NPRe':1,'QED':1})

GC_96 = Coupling(name = 'GC_96',
                 value = '-((CtaWIm*vev)/LambdaEFT**2)',
                 order = {'NP':1,'NPCtaW':1,'NPCtaWIm':1,'NPIm':1,'QED':1})

GC_97 = Coupling(name = 'GC_97',
                 value = '(CtaWIm*vev)/LambdaEFT**2',
                 order = {'NP':1,'NPCtaW':1,'NPCtaWIm':1,'NPIm':1,'QED':1})

GC_98 = Coupling(name = 'GC_98',
                 value = '(CtaWRe*complex(0,1)*vev)/LambdaEFT**2',
                 order = {'NP':1,'NPCtaW':1,'NPCtaWRe':1,'NPRe':1,'QED':1})

GC_99 = Coupling(name = 'GC_99',
                 value = '(CeBIm*cw*vev)/(LambdaEFT**2*cmath.sqrt(2))',
                 order = {'NP':1,'NPCeB':1,'NPCeBIm':1,'NPIm':1,'QED':1})

GC_100 = Coupling(name = 'GC_100',
                  value = '(CeBRe*cw*complex(0,1)*vev)/(LambdaEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPCeB':1,'NPCeBRe':1,'NPRe':1,'QED':1})

GC_101 = Coupling(name = 'GC_101',
                  value = '-((CeWIm*cw*vev)/(LambdaEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPCeW':1,'NPCeWIm':1,'NPIm':1,'QED':1})

GC_102 = Coupling(name = 'GC_102',
                  value = '-((CeWRe*cw*complex(0,1)*vev)/(LambdaEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPCeW':1,'NPCeWRe':1,'NPRe':1,'QED':1})

GC_103 = Coupling(name = 'GC_103',
                  value = '(CmuBIm*cw*vev)/(LambdaEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPCmuB':1,'NPCmuBIm':1,'NPIm':1,'QED':1})

GC_104 = Coupling(name = 'GC_104',
                  value = '(CmuBRe*cw*complex(0,1)*vev)/(LambdaEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPCmuB':1,'NPCmuBRe':1,'NPRe':1,'QED':1})

GC_105 = Coupling(name = 'GC_105',
                  value = '-((CmuWIm*cw*vev)/(LambdaEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPCmuW':1,'NPCmuWIm':1,'NPIm':1,'QED':1})

GC_106 = Coupling(name = 'GC_106',
                  value = '-((CmuWRe*cw*complex(0,1)*vev)/(LambdaEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPCmuW':1,'NPCmuWRe':1,'NPRe':1,'QED':1})

GC_107 = Coupling(name = 'GC_107',
                  value = '(CtaBIm*cw*vev)/(LambdaEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPCtaB':1,'NPCtaBIm':1,'NPIm':1,'QED':1})

GC_108 = Coupling(name = 'GC_108',
                  value = '(CtaBRe*cw*complex(0,1)*vev)/(LambdaEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPCtaB':1,'NPCtaBRe':1,'NPRe':1,'QED':1})

GC_109 = Coupling(name = 'GC_109',
                  value = '-((CtaWIm*cw*vev)/(LambdaEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPCtaW':1,'NPCtaWIm':1,'NPIm':1,'QED':1})

GC_110 = Coupling(name = 'GC_110',
                  value = '-((CtaWRe*cw*complex(0,1)*vev)/(LambdaEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPCtaW':1,'NPCtaWRe':1,'NPRe':1,'QED':1})

GC_111 = Coupling(name = 'GC_111',
                  value = '(CeWIm*ee*vev)/LambdaEFT**2',
                  order = {'NP':1,'NPCeW':1,'NPCeWIm':1,'NPIm':1,'QED':2})

GC_112 = Coupling(name = 'GC_112',
                  value = '-((CeWRe*ee*complex(0,1)*vev)/LambdaEFT**2)',
                  order = {'NP':1,'NPCeW':1,'NPCeWRe':1,'NPRe':1,'QED':2})

GC_113 = Coupling(name = 'GC_113',
                  value = '(CeWRe*ee*complex(0,1)*vev)/LambdaEFT**2',
                  order = {'NP':1,'NPCeW':1,'NPCeWRe':1,'NPRe':1,'QED':2})

GC_114 = Coupling(name = 'GC_114',
                  value = '(CmuWIm*ee*vev)/LambdaEFT**2',
                  order = {'NP':1,'NPCmuW':1,'NPCmuWIm':1,'NPIm':1,'QED':2})

GC_115 = Coupling(name = 'GC_115',
                  value = '-((CmuWRe*ee*complex(0,1)*vev)/LambdaEFT**2)',
                  order = {'NP':1,'NPCmuW':1,'NPCmuWRe':1,'NPRe':1,'QED':2})

GC_116 = Coupling(name = 'GC_116',
                  value = '(CmuWRe*ee*complex(0,1)*vev)/LambdaEFT**2',
                  order = {'NP':1,'NPCmuW':1,'NPCmuWRe':1,'NPRe':1,'QED':2})

GC_117 = Coupling(name = 'GC_117',
                  value = '(CtaWIm*ee*vev)/LambdaEFT**2',
                  order = {'NP':1,'NPCtaW':1,'NPCtaWIm':1,'NPIm':1,'QED':2})

GC_118 = Coupling(name = 'GC_118',
                  value = '-((CtaWRe*ee*complex(0,1)*vev)/LambdaEFT**2)',
                  order = {'NP':1,'NPCtaW':1,'NPCtaWRe':1,'NPRe':1,'QED':2})

GC_119 = Coupling(name = 'GC_119',
                  value = '(CtaWRe*ee*complex(0,1)*vev)/LambdaEFT**2',
                  order = {'NP':1,'NPCtaW':1,'NPCtaWRe':1,'NPRe':1,'QED':2})

GC_120 = Coupling(name = 'GC_120',
                  value = '(ee**2*complex(0,1)*vev)/(2.*sw**2)',
                  order = {'QED':1})

GC_121 = Coupling(name = 'GC_121',
                  value = '(CeWIm*ee*vev)/(LambdaEFT**2*sw*cmath.sqrt(2))',
                  order = {'NP':1,'NPCeW':1,'NPCeWIm':1,'NPIm':1,'QED':2})

GC_122 = Coupling(name = 'GC_122',
                  value = '(CeWRe*ee*complex(0,1)*vev)/(LambdaEFT**2*sw*cmath.sqrt(2))',
                  order = {'NP':1,'NPCeW':1,'NPCeWRe':1,'NPRe':1,'QED':2})

GC_123 = Coupling(name = 'GC_123',
                  value = '(CmuWIm*ee*vev)/(LambdaEFT**2*sw*cmath.sqrt(2))',
                  order = {'NP':1,'NPCmuW':1,'NPCmuWIm':1,'NPIm':1,'QED':2})

GC_124 = Coupling(name = 'GC_124',
                  value = '(CmuWRe*ee*complex(0,1)*vev)/(LambdaEFT**2*sw*cmath.sqrt(2))',
                  order = {'NP':1,'NPCmuW':1,'NPCmuWRe':1,'NPRe':1,'QED':2})

GC_125 = Coupling(name = 'GC_125',
                  value = '(CtaWIm*ee*vev)/(LambdaEFT**2*sw*cmath.sqrt(2))',
                  order = {'NP':1,'NPCtaW':1,'NPCtaWIm':1,'NPIm':1,'QED':2})

GC_126 = Coupling(name = 'GC_126',
                  value = '(CtaWRe*ee*complex(0,1)*vev)/(LambdaEFT**2*sw*cmath.sqrt(2))',
                  order = {'NP':1,'NPCtaW':1,'NPCtaWRe':1,'NPRe':1,'QED':2})

GC_127 = Coupling(name = 'GC_127',
                  value = '-((CeWIm*cw*ee*vev)/(LambdaEFT**2*sw))',
                  order = {'NP':1,'NPCeW':1,'NPCeWIm':1,'NPIm':1,'QED':2})

GC_128 = Coupling(name = 'GC_128',
                  value = '-((CeWRe*cw*ee*complex(0,1)*vev)/(LambdaEFT**2*sw))',
                  order = {'NP':1,'NPCeW':1,'NPCeWRe':1,'NPRe':1,'QED':2})

GC_129 = Coupling(name = 'GC_129',
                  value = '(CeWRe*cw*ee*complex(0,1)*vev)/(LambdaEFT**2*sw)',
                  order = {'NP':1,'NPCeW':1,'NPCeWRe':1,'NPRe':1,'QED':2})

GC_130 = Coupling(name = 'GC_130',
                  value = '-((CmuWIm*cw*ee*vev)/(LambdaEFT**2*sw))',
                  order = {'NP':1,'NPCmuW':1,'NPCmuWIm':1,'NPIm':1,'QED':2})

GC_131 = Coupling(name = 'GC_131',
                  value = '-((CmuWRe*cw*ee*complex(0,1)*vev)/(LambdaEFT**2*sw))',
                  order = {'NP':1,'NPCmuW':1,'NPCmuWRe':1,'NPRe':1,'QED':2})

GC_132 = Coupling(name = 'GC_132',
                  value = '(CmuWRe*cw*ee*complex(0,1)*vev)/(LambdaEFT**2*sw)',
                  order = {'NP':1,'NPCmuW':1,'NPCmuWRe':1,'NPRe':1,'QED':2})

GC_133 = Coupling(name = 'GC_133',
                  value = '-((CtaWIm*cw*ee*vev)/(LambdaEFT**2*sw))',
                  order = {'NP':1,'NPCtaW':1,'NPCtaWIm':1,'NPIm':1,'QED':2})

GC_134 = Coupling(name = 'GC_134',
                  value = '-((CtaWRe*cw*ee*complex(0,1)*vev)/(LambdaEFT**2*sw))',
                  order = {'NP':1,'NPCtaW':1,'NPCtaWRe':1,'NPRe':1,'QED':2})

GC_135 = Coupling(name = 'GC_135',
                  value = '(CtaWRe*cw*ee*complex(0,1)*vev)/(LambdaEFT**2*sw)',
                  order = {'NP':1,'NPCtaW':1,'NPCtaWRe':1,'NPRe':1,'QED':2})

GC_136 = Coupling(name = 'GC_136',
                  value = '-((CeBIm*sw*vev)/(LambdaEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPCeB':1,'NPCeBIm':1,'NPIm':1,'QED':1})

GC_137 = Coupling(name = 'GC_137',
                  value = '-((CeBRe*complex(0,1)*sw*vev)/(LambdaEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPCeB':1,'NPCeBRe':1,'NPRe':1,'QED':1})

GC_138 = Coupling(name = 'GC_138',
                  value = '-((CeWIm*sw*vev)/(LambdaEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPCeW':1,'NPCeWIm':1,'NPIm':1,'QED':1})

GC_139 = Coupling(name = 'GC_139',
                  value = '-((CeWRe*complex(0,1)*sw*vev)/(LambdaEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPCeW':1,'NPCeWRe':1,'NPRe':1,'QED':1})

GC_140 = Coupling(name = 'GC_140',
                  value = '-((CmuBIm*sw*vev)/(LambdaEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPCmuB':1,'NPCmuBIm':1,'NPIm':1,'QED':1})

GC_141 = Coupling(name = 'GC_141',
                  value = '-((CmuBRe*complex(0,1)*sw*vev)/(LambdaEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPCmuB':1,'NPCmuBRe':1,'NPRe':1,'QED':1})

GC_142 = Coupling(name = 'GC_142',
                  value = '-((CmuWIm*sw*vev)/(LambdaEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPCmuW':1,'NPCmuWIm':1,'NPIm':1,'QED':1})

GC_143 = Coupling(name = 'GC_143',
                  value = '-((CmuWRe*complex(0,1)*sw*vev)/(LambdaEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPCmuW':1,'NPCmuWRe':1,'NPRe':1,'QED':1})

GC_144 = Coupling(name = 'GC_144',
                  value = '-((CtaBIm*sw*vev)/(LambdaEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPCtaB':1,'NPCtaBIm':1,'NPIm':1,'QED':1})

GC_145 = Coupling(name = 'GC_145',
                  value = '-((CtaBRe*complex(0,1)*sw*vev)/(LambdaEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPCtaB':1,'NPCtaBRe':1,'NPRe':1,'QED':1})

GC_146 = Coupling(name = 'GC_146',
                  value = '-((CtaWIm*sw*vev)/(LambdaEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPCtaW':1,'NPCtaWIm':1,'NPIm':1,'QED':1})

GC_147 = Coupling(name = 'GC_147',
                  value = '-((CtaWRe*complex(0,1)*sw*vev)/(LambdaEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPCtaW':1,'NPCtaWRe':1,'NPRe':1,'QED':1})

GC_148 = Coupling(name = 'GC_148',
                  value = 'ee**2*complex(0,1)*vev + (cw**2*ee**2*complex(0,1)*vev)/(2.*sw**2) + (ee**2*complex(0,1)*sw**2*vev)/(2.*cw**2)',
                  order = {'QED':1})

GC_149 = Coupling(name = 'GC_149',
                  value = '-((complex(0,1)*yb)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_150 = Coupling(name = 'GC_150',
                  value = '-((complex(0,1)*yc)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_151 = Coupling(name = 'GC_151',
                  value = '-((complex(0,1)*ydo)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_152 = Coupling(name = 'GC_152',
                  value = '-((complex(0,1)*ye)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_153 = Coupling(name = 'GC_153',
                  value = '-((complex(0,1)*ym)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_154 = Coupling(name = 'GC_154',
                  value = '-((complex(0,1)*ys)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_155 = Coupling(name = 'GC_155',
                  value = '-((complex(0,1)*yt)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_156 = Coupling(name = 'GC_156',
                  value = '-((complex(0,1)*ytau)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_157 = Coupling(name = 'GC_157',
                  value = '-((complex(0,1)*yup)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_158 = Coupling(name = 'GC_158',
                  value = '-((ee*complex(0,1)*complexconjugate(CKM1x1))/(sw*cmath.sqrt(2)))',
                  order = {'QED':1})

GC_159 = Coupling(name = 'GC_159',
                  value = '-((ee*complex(0,1)*complexconjugate(CKM1x2))/(sw*cmath.sqrt(2)))',
                  order = {'QED':1})

GC_160 = Coupling(name = 'GC_160',
                  value = '-((ee*complex(0,1)*complexconjugate(CKM1x3))/(sw*cmath.sqrt(2)))',
                  order = {'QED':1})

GC_161 = Coupling(name = 'GC_161',
                  value = '-((ee*complex(0,1)*complexconjugate(CKM2x1))/(sw*cmath.sqrt(2)))',
                  order = {'QED':1})

GC_162 = Coupling(name = 'GC_162',
                  value = '-((ee*complex(0,1)*complexconjugate(CKM2x2))/(sw*cmath.sqrt(2)))',
                  order = {'QED':1})

GC_163 = Coupling(name = 'GC_163',
                  value = '-((ee*complex(0,1)*complexconjugate(CKM2x3))/(sw*cmath.sqrt(2)))',
                  order = {'QED':1})

GC_164 = Coupling(name = 'GC_164',
                  value = '-((ee*complex(0,1)*complexconjugate(CKM3x1))/(sw*cmath.sqrt(2)))',
                  order = {'QED':1})

GC_165 = Coupling(name = 'GC_165',
                  value = '-((ee*complex(0,1)*complexconjugate(CKM3x2))/(sw*cmath.sqrt(2)))',
                  order = {'QED':1})

GC_166 = Coupling(name = 'GC_166',
                  value = '-((ee*complex(0,1)*complexconjugate(CKM3x3))/(sw*cmath.sqrt(2)))',
                  order = {'QED':1})

