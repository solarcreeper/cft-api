<template>
  <div class="content-wrapper">
    <el-breadcrumb separator-class="el-icon-arrow-right">
      <el-breadcrumb-item :to="{ path: '/home' }">首页</el-breadcrumb-item>
      <el-breadcrumb-item>IO模型库</el-breadcrumb-item>
    </el-breadcrumb>
    <el-card class="box-card">
      <el-row :gutter="30">
        <el-col :span="4">
          <el-input v-model="query_info.io_name" placeholder="IO名称" @change="search"></el-input>
        </el-col>
        <el-col :span="4">
          <el-input v-model="query_info.tool_name" placeholder="IO工具" @change="search"></el-input>
        </el-col>
        <el-col :span="6">
          <el-input v-model="query_info.io_params" placeholder="IO参数" @change="search"></el-input>
        </el-col>
        <el-col :span="2" :push="3">
          <el-button type="primary" @click="clear">清除</el-button>
        </el-col>
        <el-col :span="2" :push="3">
          <el-button type="success">新建</el-button>
        </el-col>
        <el-col :span="2" :push="3">
          <el-button type="danger" @click="remove">删除</el-button>
        </el-col>
      </el-row>
      <el-row>
        <el-table :data="io_list" @selection-change="handleSelectionChange" border stripe>
          <el-table-column type="selection" width="35"></el-table-column>
          <el-table-column prop="io_name" label="IO名称" width="140"></el-table-column>
          <el-table-column prop="tool_name" label="IO工具" width="140"></el-table-column>
          <el-table-column prop="io_params" label="IO参数"></el-table-column>
        </el-table>
      </el-row>

      <el-pagination
        @size-change="handleSizeChange"
        @current-change="handleCurrentChange"
        :current-page="query_info.page"
        :page-sizes="[30, 50, 100]"
        :page-size="query_info.per_page"
        layout="total, sizes, prev, pager, next, jumper"
        :total="total"
      ></el-pagination>
    </el-card>
  </div>
</template>

<script>
export default {
  data () {
    return {
      query_info: {
        io_name: '',
        tool_name: '',
        io_params: '',
        page: 1,
        per_page: 30
      },
      io_list: [],
      selected_io_list: [],
      total: 0
    }
  },
  created () {
    this.getIOModuleList()
  },
  methods: {
    async getIOModuleList () {
      const { data: res } = await this.$http.get('io', { params: this.query_info })
      if (res.result !== true) {
        return this.$message({ showClose: true, message: '获取IO模型库失败', type: 'error', duration: 1000 })
      }
      this.io_list = res.data
      this.total = res.total
    },
    handleSizeChange (newSize) {
      this.query_info.per_page = newSize
      this.getIOModuleList()
    },
    handleCurrentChange (newPage) {
      this.query_info.page = newPage
      this.getIOModuleList()
    },
    handleSelectionChange (val) {
      this.selected_io_list = val
    },
    search () {
      this.getIOModuleList()
    },
    clear () {
      this.query_info.page = 1
      this.query_info.io_name = ''
      this.query_info.tool_name = ''
      this.query_info.io_params = ''
      this.getIOModuleList()
    },
    async remove () {
      if (this.selected_io_list.length === 0) {
        return this.$message({ message: '请选择需要删除得模型', type: 'error', duration: 1000 })
      }
      for (const iomodel of this.selected_io_list) {
        const codition = { io_name: iomodel.io_name }
        const { data: res } = await this.$http.delete('io', { params: codition })
        if (res.result !== true) {
          this.$message({ message: '删除IO模型失败', type: 'error', duration: 300 })
        } else {
          this.$message({ message: '删除IO模型成功', type: 'success', duration: 300 })
        }
      }
      this.getIOModuleList()
    }
  }
}
</script>

<style lang="less" scoped>
.el-table {
  min-height: 670px;
  max-height: 670px;
  overflow: auto;
}

.el-button {
  width: 90px;
}
</style>
