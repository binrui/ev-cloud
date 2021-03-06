#coding=utf-8
from django.db import models

app_label = 'network'

class VlanType(models.Model):
    code = models.AutoField('类型编号', primary_key=True)
    name = models.CharField('类型名称', max_length=100)
    order= models.IntegerField('排序', default=0, 
        help_text="用于在页面中的显示顺序，数值越小越靠前。")
    
    def __str__(self):
        return self.name
 
    class Meta:
        app_label = app_label
        verbose_name = '子网类型'
        verbose_name_plural = '3_子网类型'

class Vlan(models.Model):
    vlan    = models.CharField(max_length=100)
    br      = models.CharField(max_length=50)
    type    = models.ForeignKey(VlanType)
    enable  = models.BooleanField()
    remarks = models.TextField(null=True, blank=True)
    subnetip = models.GenericIPAddressField(null=True, blank=True)
    netmask = models.GenericIPAddressField(null=True, blank=True)
    gateway = models.GenericIPAddressField(null=True, blank=True)
    dnsserver = models.GenericIPAddressField(null=True, blank=True)
    order    = models.IntegerField('排序', default=0, 
        help_text="用于在页面中的显示顺序，数值越小越靠前。")


    def __str__(self):
    	return self.vlan
 
    class Meta:
        app_label = app_label
        verbose_name = '子网'
        verbose_name_plural = '2_子网'

class MacIP(models.Model):
    vlan    = models.ForeignKey(Vlan)
    mac     = models.CharField(max_length=17, unique = True)
    ipv4    = models.GenericIPAddressField(unique = True)
    vmid    = models.CharField(max_length=100,null=True,blank=True, default='')
    enable  = models.BooleanField(default=True)

    def __str__(self):
    	return self.mac
 
    class Meta:
        app_label = app_label
        verbose_name = 'IP地址'
        verbose_name_plural = '1_IP地址'

