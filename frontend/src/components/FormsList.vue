<template>
  <div>
    <v-row>
      <v-col>
        <h3 variant="h6" gutter-bottom>Forms</h3>
        <v-divider></v-divider>
      </v-col>
    </v-row>

    <template v-if="associatedPdfs && associatedPdfs.length > 0">
      <v-list>
        <v-list-item v-for="(pdf, index) in associatedPdfs" :key="index">
          <a @click="handlePdfClick(pdf.pdfName)" class="primary--text"  style="color: blue; cursor: pointer; word-wrap: break-word;">
            {{ pdf.label }}
          </a>
        </v-list-item>
      </v-list>
    </template>

    <template v-else>
      <body>No forms available for this lab item.</body>
    </template>
  </div>
</template>

<script>
import fetchPdf from '@/api/fetchPdf';

export default {
  props: {
    name: String,
    associatedPdfs: Array,
  },
  methods: {
    async handlePdfClick(pdfName) {
      try {
        const response = await fetchPdf(this.name, pdfName); // Adjust the parameters as needed
        if (response.ok) {
          const blob = await response.blob();
          const url = window.URL.createObjectURL(blob);
          window.open(url);
        } else {
          console.error(`Error fetching File: ${pdfName}`);
        }
      } catch (error) {
        console.error('Error fetching PDF:', error);
      }
    },
  },
};
</script>

<style scoped>
/* Add your component-specific styles here */
</style>
