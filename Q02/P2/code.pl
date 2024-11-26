#!/usr/bin/perl

use strict;
use warnings;

use Data::Dumper;

my @runes = ();
my $runic = 0;

while (my $line = <>) {
    chomp($line);
    if (@runes == 0) {
	if ($line =~ /^WORDS:(.*)$/i) {
	    foreach my $rune (split(/,/, $1)) {
		push @runes, $rune;
		$rune = reverse($rune);
		push @runes, $rune;
	    }
	    next;
	}
    }

    my %symbols = ();
    for (my $i = 0; $i < length($line); $i++) {
	foreach my $rune (@runes) {
	    my $rlen = length($rune);
	    if (substr($line, $i, $rlen) eq $rune) {
		for (my $j = 0; $j < $rlen; $j++) {
		    $symbols{$i + $j} = 1;
		}
	    }
	}
    }

    printf("Runic symbols: %d\n", scalar(keys %symbols));
    $runic += scalar(keys %symbols);
}

print("Total runic symbols: $runic\n");
