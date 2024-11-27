#!/usr/bin/perl

use strict;
use warnings;

my $sum = 0;
my $total = 0;
my $min = undef;
while (<>) {
    chomp;
    if (!defined($min) || $_ < $min) {
	$min = $_;
    }
    $sum += $_;
    $total++;
}
print("$min; $sum; $total\n");
printf("Hits needed: %d\n", $sum - $min * $total);
