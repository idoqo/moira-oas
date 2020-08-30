/* 
 * Moira Alert
 *
 * This is an API description for [Moira Alert project](https://moira.readthedocs.io/en/latest/overview.html). Please check <https://github.com/moira-alert/>
 *
 * The version of the OpenAPI document: 2.5.1.48
 * 
 * Generated by: https://github.com/openapitools/openapi-generator.git
 */

using System;
using System.IO;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.Linq;
using System.Reflection;
using RestSharp;
using NUnit.Framework;

using Org.OpenAPITools.Client;
using Org.OpenAPITools.Api;
using Org.OpenAPITools.Model;

namespace Org.OpenAPITools.Test
{
    /// <summary>
    ///  Class for testing TriggerApi
    /// </summary>
    /// <remarks>
    /// This file is automatically generated by OpenAPI Generator (https://openapi-generator.tech).
    /// Please update the test case below to test the API endpoint.
    /// </remarks>
    public class TriggerApiTests
    {
        private TriggerApi instance;

        /// <summary>
        /// Setup before each unit test
        /// </summary>
        [SetUp]
        public void Init()
        {
            instance = new TriggerApi();
        }

        /// <summary>
        /// Clean up after each unit test
        /// </summary>
        [TearDown]
        public void Cleanup()
        {

        }

        /// <summary>
        /// Test an instance of TriggerApi
        /// </summary>
        [Test]
        public void InstanceTest()
        {
            // TODO uncomment below to test 'IsInstanceOf' TriggerApi
            //Assert.IsInstanceOf(typeof(TriggerApi), instance);
        }

        
        /// <summary>
        /// Test CreateTrigger
        /// </summary>
        [Test]
        public void CreateTriggerTest()
        {
            // TODO uncomment below to test the method and replace null with proper value
            //Trigger trigger = null;
            //var response = instance.CreateTrigger(trigger);
            //Assert.IsInstanceOf(typeof(InlineResponse2009), response, "response is InlineResponse2009");
        }
        
        /// <summary>
        /// Test DeleteTrigger
        /// </summary>
        [Test]
        public void DeleteTriggerTest()
        {
            // TODO uncomment below to test the method and replace null with proper value
            //Guid triggerID = null;
            //instance.DeleteTrigger(triggerID);
            
        }
        
        /// <summary>
        /// Test DeleteTriggerMetric
        /// </summary>
        [Test]
        public void DeleteTriggerMetricTest()
        {
            // TODO uncomment below to test the method and replace null with proper value
            //Guid triggerID = null;
            //string name = null;
            //instance.DeleteTriggerMetric(triggerID, name);
            
        }
        
        /// <summary>
        /// Test DeleteTriggerNoDataMetrics
        /// </summary>
        [Test]
        public void DeleteTriggerNoDataMetricsTest()
        {
            // TODO uncomment below to test the method and replace null with proper value
            //Guid triggerID = null;
            //instance.DeleteTriggerNoDataMetrics(triggerID);
            
        }
        
        /// <summary>
        /// Test DeleteTriggerThrottling
        /// </summary>
        [Test]
        public void DeleteTriggerThrottlingTest()
        {
            // TODO uncomment below to test the method and replace null with proper value
            //Guid triggerID = null;
            //instance.DeleteTriggerThrottling(triggerID);
            
        }
        
        /// <summary>
        /// Test GetTrigger
        /// </summary>
        [Test]
        public void GetTriggerTest()
        {
            // TODO uncomment below to test the method and replace null with proper value
            //Guid triggerID = null;
            //var response = instance.GetTrigger(triggerID);
            //Assert.IsInstanceOf(typeof(Trigger), response, "response is Trigger");
        }
        
        /// <summary>
        /// Test GetTriggerMetrics
        /// </summary>
        [Test]
        public void GetTriggerMetricsTest()
        {
            // TODO uncomment below to test the method and replace null with proper value
            //Guid triggerID = null;
            //string from = null;
            //string to = null;
            //var response = instance.GetTriggerMetrics(triggerID, from, to);
            //Assert.IsInstanceOf(typeof(Dictionary<string, List<Object>>), response, "response is Dictionary<string, List<Object>>");
        }
        
        /// <summary>
        /// Test GetTriggerPlot
        /// </summary>
        [Test]
        public void GetTriggerPlotTest()
        {
            // TODO uncomment below to test the method and replace null with proper value
            //Guid triggerID = null;
            //string targetID = null;
            //string from = null;
            //string to = null;
            //var response = instance.GetTriggerPlot(triggerID, targetID, from, to);
            //Assert.IsInstanceOf(typeof(System.IO.Stream), response, "response is System.IO.Stream");
        }
        
        /// <summary>
        /// Test GetTriggerState
        /// </summary>
        [Test]
        public void GetTriggerStateTest()
        {
            // TODO uncomment below to test the method and replace null with proper value
            //Guid triggerID = null;
            //var response = instance.GetTriggerState(triggerID);
            //Assert.IsInstanceOf(typeof(TriggerCheck), response, "response is TriggerCheck");
        }
        
        /// <summary>
        /// Test GetTriggerThrottling
        /// </summary>
        [Test]
        public void GetTriggerThrottlingTest()
        {
            // TODO uncomment below to test the method and replace null with proper value
            //Guid triggerID = null;
            //var response = instance.GetTriggerThrottling(triggerID);
            //Assert.IsInstanceOf(typeof(InlineResponse20011), response, "response is InlineResponse20011");
        }
        
        /// <summary>
        /// Test GetTriggers
        /// </summary>
        [Test]
        public void GetTriggersTest()
        {
            // TODO uncomment below to test the method and replace null with proper value
            //var response = instance.GetTriggers();
            //Assert.IsInstanceOf(typeof(InlineResponse2008), response, "response is InlineResponse2008");
        }
        
        /// <summary>
        /// Test SearchTriggers
        /// </summary>
        [Test]
        public void SearchTriggersTest()
        {
            // TODO uncomment below to test the method and replace null with proper value
            //string text = null;
            //bool? onlyProblems = null;
            //int? page = null;
            //var response = instance.SearchTriggers(text, onlyProblems, page);
            //Assert.IsInstanceOf(typeof(InlineResponse20010), response, "response is InlineResponse20010");
        }
        
        /// <summary>
        /// Test SearchTriggersPage
        /// </summary>
        [Test]
        public void SearchTriggersPageTest()
        {
            // TODO uncomment below to test the method and replace null with proper value
            //string text = null;
            //bool? onlyProblems = null;
            //int? page = null;
            //var response = instance.SearchTriggersPage(text, onlyProblems, page);
            //Assert.IsInstanceOf(typeof(InlineResponse20010), response, "response is InlineResponse20010");
        }
        
        /// <summary>
        /// Test SetTriggerMaintenance
        /// </summary>
        [Test]
        public void SetTriggerMaintenanceTest()
        {
            // TODO uncomment below to test the method and replace null with proper value
            //Guid triggerID = null;
            //UNKNOWN_BASE_TYPE UNKNOWN_BASE_TYPE = null;
            //instance.SetTriggerMaintenance(triggerID, UNKNOWN_BASE_TYPE);
            
        }
        
        /// <summary>
        /// Test UpdateTrigger
        /// </summary>
        [Test]
        public void UpdateTriggerTest()
        {
            // TODO uncomment below to test the method and replace null with proper value
            //Guid triggerID = null;
            //Trigger trigger = null;
            //var response = instance.UpdateTrigger(triggerID, trigger);
            //Assert.IsInstanceOf(typeof(InlineResponse2009), response, "response is InlineResponse2009");
        }
        
    }

}
