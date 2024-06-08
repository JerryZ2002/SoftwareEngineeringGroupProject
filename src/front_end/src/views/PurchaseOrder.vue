<!-- PurchaseOrderComponent.vue -->

<template>
    <el-card class="box-card scrollable-card" style="width: 100%">
    <template #header >
      <div>
        <el-input v-model="searchKeyword" placeholder="输入关键字进行搜索" style="width: 60%"  />
        <el-select v-model="selectedField" placeholder="请选择搜索字段" style="width: 30%">
          <el-option v-for="field in availableFields" :key="field" :label="field" :value="field" />
        </el-select>
        <el-button type="primary" @click="searchPurchaseOrders" >搜索</el-button>
      </div>
      <div class="card-header" style="width: 90%;">
        
        <span>
          <el-text class="mx-1" size="large">采购清单</el-text>
        </span>
        <el-button color="#626aef" :dark="isDark" round @click="loadPurchaseOrders()">显示所有</el-button>
        <el-button color="#626aef" :dark="isDark" round @click="addPurchaseOrderpre()">添加新订单</el-button>
      </div>
    </template>

    <el-table :data="sorteDates" style="width: 80%; min-width: 800px" :max-height="400" stripe :show-header="true" :show-summary="false">
      <el-table-column prop="order_number" label="订单编号" :min-width="80" ></el-table-column>
      <el-table-column prop="product_id" label="商品编号" width="80"></el-table-column>
      <el-table-column prop="purchase_date" label="购买日期" width="100"></el-table-column>
      <el-table-column prop="unit_price" label="单价" width="80"></el-table-column>
      <el-table-column prop="quantity" label="数量" width="80"></el-table-column>
      <el-table-column prop="supplier" label="供货商" width="100"></el-table-column>
      <el-table-column prop="received" label="是否收到" width="100"></el-table-column>
      <el-table-column label="操作" width="150">
        <template #default="{ row }">
          <div style="display: flex; align-items: center; justify-content: space-between;">
            <el-button type="primary" @click="editPurchaseOrder(row)">修改</el-button>
            <el-button type="danger" @click="deletePurchaseOrder(row.order_number)">删除</el-button>
          </div>
        </template>
      </el-table-column>
    </el-table>

    <template #footer>以上为所有进货记录</template>

  </el-card>
  <div class="form-container">
    <!-- edit form -->
    <div v-if="editedOrder.order_number !== null && state === 1" class="form">
      <h3>编辑采购订单</h3>
      <form @submit.prevent="updatePurchaseOrder">

        <div class="form-row">
          <div class="form-item">
            <label for="edited-order-number">订单编号：</label>
            <el-input v-model="editedOrder.order_number" id="edited-order-number" type="number" :autosize="{ minRows: 1, maxRows: 4 }" required />
          </div>

          <div class="form-item">
            <label for="edited-product-id">商品编号：</label>
            <el-input v-model="editedOrder.product_id" id="edited-product-id" type="number" :autosize="{ minRows: 1, maxRows: 4 }" required />
          </div>

          <div class="form-item">
            <label for="edited-purchase-date">购买日期：</label>
            <el-input v-model="editedOrder.purchase_date" id="edited-purchase-date" type="date" :autosize="{ minRows: 1, maxRows: 4 }" required />
          </div>
        </div>

        <div class="form-row">
          <div class="form-item">
            <label for="edited-unit-price">单价：</label>
            <el-input v-model="editedOrder.unit_price" id="edited-unit-price" type="number" step="0.01" :autosize="{ minRows: 1, maxRows: 4 }" required />
          </div>

          <div class="form-item">
            <label for="edited-quantity">数量：</label>
            <el-input v-model="editedOrder.quantity" id="edited-quantity" type="number" :autosize="{ minRows: 1, maxRows: 4 }" required />
          </div>

          <div class="form-item">
            <label for="edited-supplier">供货商：</label>
            <el-input v-model="editedOrder.supplier" id="edited-supplier" type="text" :autosize="{ minRows: 1, maxRows: 4 }" required />
          </div>
        </div>

        <div class="form-row">
          <div class="form-item">
            <label for="edited-received">确认过是否收到：</label>
            <input v-model="editedOrder.received" id="edited-received" type="checkbox" />
          </div>

          <el-button color="#626aef" :dark="isDark" type="primary" @click="updatePurchaseOrder">上传</el-button>
        </div>

      </form>
    </div>


    <div v-if="state===2" class="form">
      <h3>添加采购订单</h3>
      <form @submit.prevent="addPurchaseOrder">

        <div class="form-row">
          <div class="form-item">
            <label for="new-order-number">订单编号：</label>
            <el-input v-model="newOrder.order_number" id="new-order-number" type="number" :autosize="{ minRows: 1, maxRows: 4 }" required />
          </div>

          <div class="form-item">
            <label for="new-product-id">商品编号：</label>
            <el-input v-model="newOrder.product_id" id="new-product-id" type="number" :autosize="{ minRows: 1, maxRows: 4 }" required />
          </div>

          <div class="form-item">
            <label for="new-purchase-date">购买日期：</label>
            <el-input v-model="newOrder.purchase_date" id="new-purchase-date" type="date" :autosize="{ minRows: 1, maxRows: 4 }" required />
          </div>
        </div>

        <div class="form-row">
          <div class="form-item">
            <label for="new-unit-price">单价：</label>
            <el-input v-model="newOrder.unit_price" id="new-unit-price" type="number" step="0.01" :autosize="{ minRows: 1, maxRows: 4 }" required />
          </div>

          <div class="form-item">
            <label for="new-quantity">数量：</label>
            <el-input v-model="newOrder.quantity" id="new-quantity" type="number" :autosize="{ minRows: 1, maxRows: 4 }" required />
          </div>

          <div class="form-item">
            <label for="new-supplier">供货商：</label>
            <el-input v-model="newOrder.supplier" id="new-supplier" type="text" :autosize="{ minRows: 1, maxRows: 4 }" required />
          </div>
        </div>

        <div class="form-row">
          <div class="form-item">
            <label for="new-received">确认过是否收到：</label>
            <input v-model="newOrder.received" id="new-received" type="checkbox" />
          </div>

          <el-button color="#626aef" :dark="isDark" type="primary" @click="addPurchaseOrder">上传</el-button>
        </div>

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
      availableFields: ["order_number", "purchase_date", "unit_price", "quantity", "supplier"],
      state: 0,
      purchaseOrders: [],
      PRE: [],
      ifadd : false,
      newOrder: {
        order_number: null,
        product_id: null,
        purchase_date: '',
        unit_price: null,
        quantity: null,
        supplier: null,
        received: 0,
      },
      editedOrder: {
        order_number: null,
        product_id: null,
        purchase_date: '',
        unit_price: null,
        quantity: null,
        supplier: null,
        received: 0,
      },
    };

  },
  mounted() {
    this.loadPurchaseOrders();
  },
  methods: {
    loadPurchaseOrders() {
      axios.get('http://127.0.0.1:8000/your_app_name/api/purchase-orders/')
          .then(response => {
            const sortedData = response.data.sort((a, b) => {
              if ( new Date(a.purchase_date) < new Date(b.purchase_date) ) {
                return -1;
              } else if ( new Date(a.purchase_date) > new Date(b.purchase_date) ) {
                return 1;
              } else {
                if ( a.order_number < b.order_number ) {
                  return -1;
                } else {
                  return 1;
                }
              }
            });
            this.purchaseOrders = sortedData;
          })
          .catch(error => {
            console.error('Error:', error);
          });
    },
    addPurchaseOrderpre() {
      if(this.state===2){
        this.state=0;
      }
      else{
        this.state=2;
      }
    },
    searchPurchaseOrders() {
      axios.get(`http://127.0.0.1:8000/your_app_name/api/purchase-orders/search/?query=${this.searchKeyword}&field=${this.selectedField}`)
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
            this.purchaseOrders = sortedData;
          })
          .catch(error => {
            console.error('Error:', error);
          });
    },
    addPurchaseOrder() {
      axios.post('http://127.0.0.1:8000/your_app_name/api/purchase-orders/', this.newOrder)
          .then(response => {
            console.log('Success:', response.data);
            this.loadPurchaseOrders();
            this.newOrder= {
              order_number: null,
                  product_id: null,
                  purchase_date: '',
                  unit_price: null,
                  quantity: null,
                  supplier: null,
                  received: 0,
            };
            this.ifadd = !this.ifadd;
          })
          .catch(error => {
            console.error('Error:', error);
          });
    },
    deletePurchaseOrder(orderNumber) {
      axios.delete(`http://127.0.0.1:8000/your_app_name/api/purchase-orders/${orderNumber}/`)
          .then(response => {
            if (response.status === 204) {
              console.log('Success: Purchase Order deleted');
              this.loadPurchaseOrders();
            } else {
              console.error('Error:', response.status);
            }
          })
          .catch(error => {
            console.error('Error:', error);
          });
    },
    editPurchaseOrder(order) {
      // load the order to be edited
      this.editedOrder = { ...order };
      this.state=1;
    },
    updatePurchaseOrder() {
      // send the updated order to the server
      axios.patch(`http://127.0.0.1:8000/your_app_name/api/purchase-orders/${this.editedOrder.order_number}/`, this.editedOrder)
          .then(response => {
            console.log('Success:', response.data);
            this.loadPurchaseOrders(); // reload the orders
            this.editedOrder = { // reset the form
              order_number: null,
              product_id: null,
              purchase_date: '',
              unit_price: null,
              quantity: null,
              supplier: null,
              received: 1,
            };
          })
          .catch(error => {
            console.error('Error:', error);
          });
    },

  },
  computed: {
      sorteDates() {
        return this.purchaseOrders.sort((a, b) => {
          if ( new Date(a.purchase_date) < new Date(b.purchase_date) ) {
            return -1;
          } else if ( new Date(a.purchase_date) > new Date(b.purchase_date) ) {
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
.form-container {
  display: flex;
  justify-content: space-between;
}
.form {
  margin-top: 20px;
}
.form-row {
  display: flex;
  justify-content: space-between;
  margin-bottom: 10px;
}
.form-item {
  flex-basis: 30%; 
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