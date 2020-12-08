# this manifest  kills a process named killmenow

exec { 'killmenow':
  pkill => 'killmenow',

}