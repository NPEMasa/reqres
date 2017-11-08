<?php

$string ="<html><head><title>testanddeploy</title></head><body><h1>HTML is very easy</h1><p>easy modal...</p></body></html>";

print preg_match_all('/<([^>]*)>/s', $string);
#print preg_match_all('/<([^>]*)>/s', $string, $match);
#print ($match);
?>
