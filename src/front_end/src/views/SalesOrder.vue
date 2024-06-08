<!-- PurchaseOrderComponent.vue -->

<template>
  <el-card class="box-card scrollable-card" style="width: 100%">
    <template #header>
      <div>
        <el-input v-model="searchKeyword" placeholder="输入关键字进行搜索" style="width: 60%"  />
        <el-select v-model="selectedField" placeholder="请选择搜索字段" style="width: 30%">
          <el-option v-for="field in availableFields" :key="field" :label="field" :value="field" />
        </el-select>
        <el-button type="primary" @click="searchPurchaseOrders" >搜索</el-button>
      </div>
      <div class="card-header" style="width: 90%;">
      <span>
        <el-text class="mx-1" size="large">
          销售订单
        </el-text>
      </span>
        <el-button color="#626aef" :dark="isDark" round @click="loadSalesOrders()">显示所有</el-button>
        <el-button color="#626aef" :dark="isDark" round @click="addPurchaseOrderpre">添加新销售单</el-button>
      </div>
    </template>
    <el-table :data="salesOrders" style="width: 90%; min-width: 800px" :max-height="400" stripe :show-header="true" :show-summary="false">
      <el-table-column prop="order_number" label="订单编号" :min-width="80"></el-table-column>
      <el-table-column prop="product_id" label="商品编号" :min-width="80"></el-table-column>
      <el-table-column prop="sales_date" label="出售日期" :min-width="80"></el-table-column>
      <el-table-column prop="unit_price" label="单价" :min-width="80"></el-table-column>
      <el-table-column prop="quantity" label="数量" :min-width="80"></el-table-column>
      <el-table-column label="操作" width="180">
        <template #default="{ row }">
          <div style="display: flex; align-items: center; justify-content: space-between;">
            <el-button type="primary" @click="editSalesOrder(row)">修改</el-button>
            <el-button type="danger" @click="deletePurchaseOrder(row.order_number)">删除</el-button>
          </div>
        </template>
      </el-table-column>
    </el-table>
    <template #footer>以上为所有销售记录</template>
  </el-card>


  <div>
    <!-- 编辑表单 -->
    <div v-if="editedOrder.order_number !== null && state===1">
      <h3>编辑销售订单</h3>
      <form @submit.prevent="updateSalesOrder">

        <el-row>
          <el-col :span="12">
            <el-form-item label="订单编号" prop="order_number">
              <el-input v-model="editedOrder.order_number" type="number" :autosize="{ minRows: 1, maxRows: 4 }" required />
            </el-form-item>
          </el-col>

          <el-col :span="12">
            <el-form-item label="商品编号" prop="product_id">
              <el-input v-model="editedOrder.product_id" type="number" :autosize="{ minRows: 1, maxRows: 4 }" required />
            </el-form-item>
          </el-col>
        </el-row>

        <el-row>
          <el-col :span="12">
            <el-form-item label="出售日期" prop="sales_date">
              <el-input v-model="editedOrder.sales_date" type="date" :autosize="{ minRows: 1, maxRows: 4 }" required />
            </el-form-item>
          </el-col>

          <el-col :span="6">
            <el-form-item label="单价" prop="unit_price">
              <el-input v-model="editedOrder.unit_price" type="number" step="0.01" :autosize="{ minRows: 1, maxRows: 4 }" required />
            </el-form-item>
          </el-col>

          <el-col :span="6">
            <el-form-item label="数量" prop="quantity">
              <el-input v-model="editedOrder.quantity" type="number" :autosize="{ minRows: 1, maxRows: 4 }" required />
            </el-form-item>
          </el-col>
        </el-row>

        <el-form-item>
          <el-button color="#626aef" :dark="isDark" type="primary" @click="updateSalesOrder">上传</el-button>
        </el-form-item>

      </form>
    </div>


    <div v-if="state===2">
      <h3>添加销售订单</h3>
      <form @submit.prevent="addPurchaseOrder">

        <el-row>
          <el-col :span="12">
            <el-form-item label="订单编号" prop="order_number">
              <el-input v-model="newOrder.order_number" id="edited-order-number" type="number" :autosize="{ minRows: 1, maxRows: 4 }" required />
            </el-form-item>
          </el-col>

          <el-col :span="12">
            <el-form-item label="商品编号" prop="product_id">
              <el-input v-model="newOrder.product_id" id="edited-product-id" type="number" :autosize="{ minRows: 1, maxRows: 4 }" required />
            </el-form-item>
          </el-col>
        </el-row>

        <el-row>
          <el-col :span="12">
            <el-form-item label="出售日期" prop="sales_date">
              <el-input v-model="newOrder.sales_date" id="edited-sales-date" type="date" :autosize="{ minRows: 1, maxRows: 4 }" required />
            </el-form-item>
          </el-col>

          <el-col :span="6">
            <el-form-item label="单价" prop="unit_price">
              <el-input v-model="newOrder.unit_price" id="edited-unit-price" type="number" step="0.01" :autosize="{ minRows: 1, maxRows: 4 }" required />
            </el-form-item>
          </el-col>

          <el-col :span="6">
            <el-form-item label="数量" prop="quantity">
              <el-input v-model="newOrder.quantity" id="edited-quantity" type="number" :autosize="{ minRows: 1, maxRows: 4 }" required />
            </el-form-item>
          </el-col>
        </el-row>

        <el-form-item>
          <el-button color="#626aef" :dark="isDark" type="primary" @click="addPurchaseOrder">上传</el-button>
        </el-form-item>

      </form>
    </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        searchKeyword : "",
        selectedField: null,
        availableFields: ["order_number", "sales_date", "unit_price", "quantity"],
        ifadd : false,
        salesOrders: [],
        state: 1,
        newOrder: {
          order_number: null,
          product_id: null,
          sales_date: '',
          unit_price: null,
          quantity: null,
        },
        editedOrder: {
          order_number: null,
          product_id: null,
          sales_date: '',
          unit_price: null,
          quantity: null,
        },
      };
  
    },
    mounted() {
      this.loadSalesOrders();
    },
    methods: {
      loadSalesOrders() {
        axios.get('http://127.0.0.1:8000/your_app_name/api/sales-orders/')
            .then(response => {
              this.salesOrders = response.data;
              this.sorteDates();
            })
            .catch(error => {
              console.error('Error:', error);
            });
      },
      addPurchaseOrderpre() {
        if(this.state!==2){
          this.state=2;
        }
        else this.state=0;
      },
      addPurchaseOrder() {
        axios.post('http://127.0.0.1:8000/your_app_name/api/sales-orders/', this.newOrder)
            .then(response => {
              console.log('Success:', response.data);
              this.loadSalesOrders();
              this.newOrder= {
                order_number: null,
                    product_id: null,
                    sales_date: '',
                    unit_price: null,
                    quantity: null,
              };
              this.ifadd = !this.ifadd;
            })
            .catch(error => {
              console.error('Error:', error);
            });
      },
      searchPurchaseOrders() {
      axios.get(`http://127.0.0.1:8000/your_app_name/api/sales-orders/search/?query=${this.searchKeyword}&field=${this.selectedField}`)
          .then(response => {
            const sortedData = response.data.sort((a, b) => {
              if (new Date(a.purchase_date) < new Date(b.purchase_date)) {
                return -1;
              } else if (new Date(a.purchase_date) > new Date(b.purchase_date)) {
                return 1;
              } else {
                if (a.order_number < b.order_number) {
                  return -1;
                } else {
                  return 1;
                }
              }
            });
            this.salesOrders = sortedData;
          })
          .catch(error => {
            console.error('Error:', error);
          });
    },
      deletePurchaseOrder(orderNumber) {
        axios.delete(`http://127.0.0.1:8000/your_app_name/api/sales-orders/${orderNumber}/`)
            .then(response => {
              if (response.status === 204) {
                console.log('Success: Purchase Order deleted');
                this.loadSalesOrders();
              } else {
                console.error('Error:', response.status);
              }
            })
            .catch(error => {
              console.error('Error:', error);
            });
      },
      editSalesOrder(order) {
        // load the order-info to form
        this.editedOrder = { ...order };
        this.state=1;
      },
      updateSalesOrder() {
        // send the updated order-info to the server
        axios.patch(`http://127.0.0.1:8000/your_app_name/api/sales-orders/${this.editedOrder.order_number}/`, this.editedOrder)
            .then(response => {
              console.log('Success:', response.data);
              this.loadSalesOrders(); // reload the order list
              this.editedOrder = { // reset the edited order
                order_number: null,
                product_id: null,
                sales_date: '',
                unit_price: null,
                quantity: null,
              };
            })
            .catch(error => {
              console.error('Error:', error);
            });
      },
  
    },
    computed: {
        sorteDates() {
          return this.salesOrders.sort((a, b) => {
            if ( new Date(a.sales_date) < new Date(b.sales_date) ) {
              return -1;
            } else if ( new Date(a.sales_date) > new Date(b.sales_date) ) {
              return 1;
            } else {
              if ( a.order_number < b.order_number ) {
                return -1;
              } else {
                return 1;
              }
            }
          });
        },
      },
  };
  </script>

<style>  
.card-header {  
  display: flex;  
  justify-content: space-between;  
  align-items: center;  
}  
    
.text {  
  font-size: 14px;  
}  
    
.item {  
  margin-bottom: 18px;  
}  
    
.box-card {
  width: 800px;
  height: 630px;
}
    
.scrollable-card {  
  overflow: auto;
}  
</style>