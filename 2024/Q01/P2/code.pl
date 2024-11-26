#!/usr/bin/perl

use strict;
use warnings;

my %needed = (
    'A' => 0,
    'B' => 1,
    'C' => 3,
    'D' => 5,
    'x' => 0,
    );
my $potions = 0;

while (my $line = <>) {
    chomp($line);
    for (my $i = 0; $i < length($line); $i += 2) {
	my $letter1 = substr($line, $i,     1);
	my $letter2 = substr($line, $i + 1, 1);
	my $needed = $needed{$letter1} + $needed{$letter2};
	if ($letter1 ne 'x' && $letter2 ne 'x') {
	    $needed += 2;
	}
	$potions += $needed;
    }
}
print("Potions needed: $potions\n");
