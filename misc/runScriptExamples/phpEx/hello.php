<?php

print "Hello World\n";
print "Command Line Arguments:\n";
foreach($argv as $k => $v) {
  printf("argv[%2d] = %s\n", $k, $v);
}

?>