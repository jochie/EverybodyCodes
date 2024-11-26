#!/usr/bin/perl

use strict;
use warnings;

my %needed = (
    'A' => 0,
    'B' => 1,
    'C' => 3
    );
my $potions = 0;

while (my $line = <>) {
    chomp($line);
    for (my $i = 0; $i < length($line); $i++) {
	my $letter = substr($line, $i, 1);
	$potions += $needed{$letter};
    }
}
print("Potions needed: $potions\n");
