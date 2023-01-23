#!/usr/bin/node
imported  = require( './100-data.js' ) ;
console.log ( imported.list ) ;
console.log ( imported.list.map( ( x ,  i )  =>  x  *  i ) ) ;
