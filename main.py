import pretty_midi
from MetricClass import Metrics
from UtilityFunctions import get_pattern
from MIDIFunctions import plot_beats



# Datasets

# Povel & Essens patterns
pm_PovEss = pretty_midi.PrettyMIDI('./data/Povel&Essens 1985/Povel&Essens - 1.mid')

# Essens patterns
pm_Ess = pretty_midi.PrettyMIDI('./data/Essens 1995/Essens - 1.mid')

# Fitch & Rosenveld patterns
pm_FitRos = pretty_midi.PrettyMIDI('./data/Fitch&Rosenfeld 2007/Fitch&Rosenfeld - 15.mid')



# Select a single pattern for rhythmic complexity analysis
pm = pm_FitRos



# metrical grid informations (duration of metric units in seconds)
duration = 2                       #bar
tactus = duration/4                #quarter note
tatum = tactus/4                   #sixteenth note
length = int(duration/tatum)       #16


# Pattern information
print('\n\n### PATTERN INFORMATION ###')
onsets_times = pm.get_onsets()
print('This pattern onsets positions in seconds are: ', onsets_times)
onsets_indeces = (onsets_times/tatum).astype(int)
print('Meaning that in the grid they are at positions: ', onsets_indeces)


# Instantiate a metric class
metrics = Metrics(length, onsets_indeces)



# Plot the pattern in piano roll with beats
plot_beats(pm, 45, 70)

# Print the pattern as a binary sequence
pattern = get_pattern(length, onsets_indeces)
print('The pattern is:    ', pattern)


# Rhythmic complexity analysis

##---METRICAL MEASURES----##

# Toussaint Complexity
Toussaint_OnsetNorm, Toussaint_PulseNorm, Toussaint_PulseOnsetNorm = metrics.getToussaintComplexity()

# Palmer & Krumhansl MUS 
PalmerKrumhansl_MUS_OnsetNorm, PalmerKrumhansl_MUS_PulseNorm, PalmerKrumhansl_MUS_PulseOnsetNorm = metrics.getPalmerKrumhanslMUSComplexity()

# Palmer & Krumhansl NON-MUS 
PalmerKrumhansl_NONMUS_OnsetNorm, PalmerKrumhansl_NONMUS_PulseNorm, PalmerKrumhansl_NONMUS_PulseOnsetNorm = metrics.getPalmerKrumhanslNONMUSComplexity()

# Euler
Euler_OnsetNorm, Euler_PulseNorm, Euler_PulseOnsetNorm = metrics.getEulerComplexity()

# Longuet-Higgins & Lee
LonguetHigginsLee = metrics.getLonguetHigginsLeeComplexity()

# Fitch & Rosenfeld
FitchRosenfeld = metrics.getFitchRosenfeldComplexity()

# Smith & Honing
SmithHoning = metrics.getSmithHoningComplexity()


##---PATTERN MATCHING MESURES---##

# Pressing 
Pressing = metrics.getPressingComplexity()

# Tanguiane
Tanguiane = metrics.getTanguianeComplexity()

# Keith
Keith = metrics.getKeithComplexity()


##---DISTANCE MEASURES---##

# Directed Swap Distance
DirectedSwapDistance_m2, DirectedSwapDistance_m4, DirectedSwapDistance_m8, DirectedSwapDistance_mean = metrics.getDirectedSwapDistanceComplexity()

# Weighted Note to Beat Distance
WNBD = metrics.getWeightedNotetoBeatDistance()


##---INFORMATION ENTROPY---##

# H (k-span) 
HkSpan = metrics.getHkSpanComplexity()

# H (run-span)
HrunSpan = metrics.getHrunSpanComplexity()

# Coded Element Processing System
CodedElementProcessingSystem = metrics.getCEPSComplexity()

# Lempel-Ziv Coding
LempelZiv = metrics.getLempelZivCodingComplexity()


##---INTERONSET INTERVAL HISTOGRAMS---##

# IOI Standard Deviation 
StandardDeviation_globalIOI, StandardDeviation_localIOI = metrics.getStandardDeviationComplexity()

# IOI Information Entropy
InformationEntropy_globalIOI, InformationEntropy_localIOI = metrics.getInformationEntropyComplexity()

# Tallest Bin
TallestBin_globalIOI, TallestBin_localIOI = metrics.getTallestBinComplexity()


##---MATHEMATICAL IRREGULARITY---##

# Toussaint Off-Beatness
OffBeatness = metrics.getOffBeatnessComplexity()

# Rhythmic Oddity
RhythmicOddity = metrics.getRhythmicOddityComplexity()
