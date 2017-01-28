#!/bin/bash

read D1 D2 D3 D4 ID <<<$(xprop -root _NET_ACTIVE_WINDOW); xprop -id $ID WM_NAME

