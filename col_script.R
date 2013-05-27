h_o<-read.table("genus_only.csv")
for (i in 1:length(h_o[,1])){
  thisname <- h_o[i,1]
  out <- col_children(name=thisname, checklist="2012")
  fi <- paste(thisname, i, sep="")
  write.table(out, row.names=F,col.names =F,file = fi, sep=",")
}