DIgital ausdio plugins
Electronic music, apply filters to the tracks, it changes how the track sounds
Build band pass filter
Filter has upper limit and the lower limit
if upper limit - change to the upper limit value

value goes

lower - 40
upper limit - 1000 - if a user provides these limits, then you need to overrite

Input: Soun wave - collection of frequencies - array 

input - [60,10,45,60,1500]
output - [60,40,45,60,1000]

input - [60,10,45,60,1500],20,50
output - [50,20,45,50,50]

input - []
output - Error "No frequencies supplied"

