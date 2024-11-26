#!/usr/bin/perl

use strict;
use warnings;

my @runes = ();
my $runic = 0;

while (<>) {
    chomp;
    if (@runes == 0) {
	if (/^WORDS:(.*)$/i) {
	    @runes = split(/,/, $1);
	    next;
	}
    }
    my @words = split(/ /, $_);
    foreach my $word (@words) {
	foreach my $rune (@runes) {
	    if ($word =~ /$rune/i) {
		$runic++;
	    }
	}
    }
}

print("Runic words: $runic\n");
