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
    for (my $i = 0; $i < length($line); $i += 3) {
	my $letter1 = substr($line, $i,     1);
	my $letter2 = substr($line, $i + 1, 1);
	my $letter3 = substr($line, $i + 2, 1);
	my $needed = $needed{$letter1} + $needed{$letter2} + $needed{$letter3};
	my $empties = ($letter1 eq 'x') + ($letter2 eq 'x') + ($letter3 eq 'x');
	if ($empties == 0) {
	    $needed += 2 * 3;
	} elsif ($empties == 1) {
	    $needed += 2;
	}
	$potions += $needed;
    }
}
print("Potions needed: $potions\n");
