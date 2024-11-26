#!/usr/bin/perl

use strict;
use warnings;

my @runes = ();
my $runic = 0;

my $line = <>;
chomp($line);
if ($line =~ /^WORDS:(.*)$/i) {
    @runes = ();
    my @list = split(/,/, $1);
    foreach my $rune (@list) {
	push @runes, $rune;
	$rune = reverse($rune);
	push @runes, $rune;
    }
}

# Skip empty line
<>;

# Read grid:
my @grid = ();
my @scales = ();

# Remember the original length, but have 3 copies of each line, to
# look for runes that cross over
my $armour_length = 0;
while (<>) {
    chomp;
    $armour_length = length($_);
    push @grid, $_ x 3;
    push @scales, '.' x length($_ x 3);
}

# Analysis:
for (my $r = 0; $r < @grid; $r++) {
    for (my $c = 0; $c < length($grid[$r]); $c++) {
	for my $rune (@runes) {
	    if (substr($grid[$r], $c, length($rune)) eq $rune) {
		for (my $i = 0; $i < length($rune); $i++) {
		    substr($scales[$r], $c + $i, 1) = 'X';
		}
	    }
	    my $match = 1;
	    for (my $i = 0; $i < length($rune); $i++) {
		if ($r + $i >= @grid) {
		    $match = 0;
		    last;
		}
		if (substr($grid[$r + $i], $c, 1) ne substr($rune, $i, 1)) {
		    $match = 0;
		    last;
		}
	    }
	    if ($match) {
		for (my $i = 0; $i < length($rune); $i++) {
		    substr($scales[$r + $i], $c, 1) = 'X';
		}
	    }
	}
    }
}

# Now check only 1 of the 3 copies and count the marks
my $scales = 0;
for (my $r = 0; $r < @grid; $r++) {
    for (my $c = 0; $c < $armour_length; $c++) {
	if (substr($scales[$r], $c + $armour_length, 1) eq 'X') {
	    $scales++;
	}
    }
}

print("Scales: $scales\n");
