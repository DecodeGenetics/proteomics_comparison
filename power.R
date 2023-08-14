


pwr <- function(Ne,eff,maf){
    h=2*eff^2*maf*(1-maf)
    a=pchisq(threshold,df=1,lower.tail=FALSE,ncp=Ne*h)
    return(sum(a))
    }

