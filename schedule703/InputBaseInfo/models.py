from django.db import models

# Create your models here.

# Create your models here.
#订单信息表参考0602数据导入
class OrdersMessage(models.Model):
    # order_id=models.CharField(max_length=100, verbose_name='序号',blank=True,null=True)
    order_code = models.CharField(max_length=100, verbose_name='订单编号',blank=True,null=True)
    material_code = models.CharField(max_length=100, verbose_name='物料编码',blank=True,null=True)
    material_name = models.CharField(max_length=100, verbose_name='物料名称',blank=True,null=True)
    orders_num = models.CharField(max_length=100, verbose_name='订单数量',blank=True,null=True)
    number_unit= models.CharField(max_length=100, verbose_name='数量单位',blank=True,null=True)
    customer_finish_date = models.CharField(max_length=100, verbose_name='客户交期',blank=True,null=True)
    types = models.CharField(max_length=100, verbose_name='规格', blank=True, null=True)
    order_types = models.CharField(max_length=100, verbose_name='型号', blank=True, null=True)
    customer_name = models.CharField(max_length=100, verbose_name='客户名称', blank=True, null=True)
    sales_type = models.CharField(max_length=100, verbose_name='销售类型', blank=True, null=True)
    # main_peple = models.CharField(max_length=100, verbose_name='负责人', blank=True, null=True)
    # finish_order_date = models.CharField(max_length=100, verbose_name='收单日期', blank=True, null=True)
    # finish_check_date = models.CharField(max_length=100, verbose_name='评审交期', blank=True, null=True)
    # importances = models.CharField(max_length=100, verbose_name='优先级', blank=True, null=True)
    # order_state = models.CharField(max_length=100, verbose_name='订单状态', blank=True, null=True)
    # abnormal_orders = models.CharField(max_length=100, verbose_name='异常订单', blank=True, null=True)
    # finished_process = models.CharField(max_length=100, verbose_name='已完成工序',blank=True,null=True)
    def __str__(self):
        return "<订单信息:{}>".format(self.id)
    class Meta:
        verbose_name = verbose_name_plural = '订单信息'