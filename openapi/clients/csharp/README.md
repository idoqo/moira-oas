# Org.OpenAPITools - the C# library for the Moira Alert

This is an API description for [Moira Alert project](https://moira.readthedocs.io/en/latest/overview.html). Please check <https://github.com/moira-alert/>

This C# SDK is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 2.5.1.48
- SDK version: 1.0.0
- Build package: org.openapitools.codegen.languages.CSharpClientCodegen

## Frameworks supported


- .NET 4.0 or later
- Windows Phone 7.1 (Mango)

## Dependencies


- [RestSharp](https://www.nuget.org/packages/RestSharp) - 105.1.0 or later
- [Json.NET](https://www.nuget.org/packages/Newtonsoft.Json/) - 7.0.0 or later
- [JsonSubTypes](https://www.nuget.org/packages/JsonSubTypes/) - 1.2.0 or later

The DLLs included in the package may not be the latest version. We recommend using [NuGet](https://docs.nuget.org/consume/installing-nuget) to obtain the latest version of the packages:

```
Install-Package RestSharp
Install-Package Newtonsoft.Json
Install-Package JsonSubTypes
```

NOTE: RestSharp versions greater than 105.1.0 have a bug which causes file uploads to fail. See [RestSharp#742](https://github.com/restsharp/RestSharp/issues/742)

## Installation

Run the following command to generate the DLL

- [Mac/Linux] `/bin/sh build.sh`
- [Windows] `build.bat`

Then include the DLL (under the `bin` folder) in the C# project, and use the namespaces:

```csharp
using Org.OpenAPITools.Api;
using Org.OpenAPITools.Client;
using Org.OpenAPITools.Model;

```


## Packaging

A `.nuspec` is included with the project. You can follow the Nuget quickstart to [create](https://docs.microsoft.com/en-us/nuget/quickstart/create-and-publish-a-package#create-the-package) and [publish](https://docs.microsoft.com/en-us/nuget/quickstart/create-and-publish-a-package#publish-the-package) packages.

This `.nuspec` uses placeholders from the `.csproj`, so build the `.csproj` directly:

```
nuget pack -Build -OutputDirectory out Org.OpenAPITools.csproj
```

Then, publish to a [local feed](https://docs.microsoft.com/en-us/nuget/hosting-packages/local-feeds) or [other host](https://docs.microsoft.com/en-us/nuget/hosting-packages/overview) and consume the new package via Nuget as usual.


## Getting Started

```csharp
using System.Collections.Generic;
using System.Diagnostics;
using Org.OpenAPITools.Api;
using Org.OpenAPITools.Client;
using Org.OpenAPITools.Model;

namespace Example
{
    public class Example
    {
        public static void Main()
        {

            Configuration.Default.BasePath = "http://localhost:8080/api";
            var apiInstance = new ConfigApi(Configuration.Default);

            try
            {
                // Get available configuration
                InlineResponse200 result = apiInstance.GetConfig();
                Debug.WriteLine(result);
            }
            catch (ApiException e)
            {
                Debug.Print("Exception when calling ConfigApi.GetConfig: " + e.Message );
                Debug.Print("Status Code: "+ e.ErrorCode);
                Debug.Print(e.StackTrace);
            }

        }
    }
}
```

## Documentation for API Endpoints

All URIs are relative to *http://localhost:8080/api*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ConfigApi* | [**GetConfig**](docs/ConfigApi.md#getconfig) | **GET** /config | Get available configuration
*ContactApi* | [**CreateNewContact**](docs/ContactApi.md#createnewcontact) | **PUT** /contact | Creates a new contact notification for the current user.
*ContactApi* | [**DeleteContact**](docs/ContactApi.md#deletecontact) | **DELETE** /contact/{contactId} | Deletes notification contact for the current user and remove the contact ID from all subscriptions.
*ContactApi* | [**GetContacts**](docs/ContactApi.md#getcontacts) | **GET** /contact | Gets all Moira contacts.
*ContactApi* | [**TestContactNotification**](docs/ContactApi.md#testcontactnotification) | **POST** /contact/{contactId}/test | Push a test notification to verify that the contact is properly set up.
*ContactApi* | [**UpdateContact**](docs/ContactApi.md#updatecontact) | **PUT** /contact/{contactId} | Updates an existing notification contact to the values passed in the request body.
*EventApi* | [**DeleteEvents**](docs/EventApi.md#deleteevents) | **DELETE** /event/all | Deletes all notification events
*EventApi* | [**GetTriggerEvents**](docs/EventApi.md#gettriggerevents) | **GET** /event/{triggerID} | Gets all trigger events for current page and their count
*HealthApi* | [**GetNotifierState**](docs/HealthApi.md#getnotifierstate) | **GET** /health/notifier | Get notifier state
*HealthApi* | [**UpdateNotifierState**](docs/HealthApi.md#updatenotifierstate) | **PUT** /health/notifier | Update notifier state
*NotificationsApi* | [**DeleteAllNotification**](docs/NotificationsApi.md#deleteallnotification) | **DELETE** /notification/all | deletes all available notifications
*NotificationsApi* | [**DeleteNotification**](docs/NotificationsApi.md#deletenotification) | **DELETE** /notification | delete a notification by id
*NotificationsApi* | [**GetNotifications**](docs/NotificationsApi.md#getnotifications) | **GET** /notification | gets a paginated list of notifications, all notifications are fetched if end = -1 and start = 0
*PatternApi* | [**DeletePattern**](docs/PatternApi.md#deletepattern) | **DELETE** /pattern/{pattern} | Deletes a Moira pattern
*PatternApi* | [**GetAllPatterns**](docs/PatternApi.md#getallpatterns) | **GET** /pattern | Get all patterns
*SubscriptionApi* | [**CreateSubscription**](docs/SubscriptionApi.md#createsubscription) | **PUT** /subscription | create a new subscription
*SubscriptionApi* | [**DeleteSubscription**](docs/SubscriptionApi.md#deletesubscription) | **DELETE** /subscription/{subscriptionId} | deletes a subscription
*SubscriptionApi* | [**GetSubscriptions**](docs/SubscriptionApi.md#getsubscriptions) | **GET** /subscription | get all subscriptions
*SubscriptionApi* | [**TestSubscriptionNotification**](docs/SubscriptionApi.md#testsubscriptionnotification) | **PUT** /subscription/{subscriptionId}/test | send test notification for a subscription
*SubscriptionApi* | [**UpdateSubscription**](docs/SubscriptionApi.md#updatesubscription) | **PUT** /subscription/{subscriptionId} | update a subscription
*TagApi* | [**DeleteTag**](docs/TagApi.md#deletetag) | **DELETE** /tag/{tag} | remove a tag
*TagApi* | [**GetTags**](docs/TagApi.md#gettags) | **GET** /tag | get all tags
*TagApi* | [**GetTagsSubscriptions**](docs/TagApi.md#gettagssubscriptions) | **GET** /tag/stats | get all tags and subscriptions
*TriggerApi* | [**CreateTrigger**](docs/TriggerApi.md#createtrigger) | **PUT** /trigger | create new trigger
*TriggerApi* | [**DeleteTrigger**](docs/TriggerApi.md#deletetrigger) | **DELETE** /trigger/{triggerID} | remove a trigger
*TriggerApi* | [**DeleteTriggerMetric**](docs/TriggerApi.md#deletetriggermetric) | **DELETE** /trigger/{triggerID}/metrics | deletes metric from last check and all trigger pattern metrics
*TriggerApi* | [**DeleteTriggerNoDataMetrics**](docs/TriggerApi.md#deletetriggernodatametrics) | **DELETE** /trigger/{triggerID}/metrics/nodata | deletes all metrics from last data which are in NODATA state. It also deletes all trigger patterns of those metrics
*TriggerApi* | [**DeleteTriggerThrottling**](docs/TriggerApi.md#deletetriggerthrottling) | **DELETE** /trigger/{triggerID}/throttling | Deletes throttling for a trigger
*TriggerApi* | [**GetTrigger**](docs/TriggerApi.md#gettrigger) | **GET** /trigger/{triggerID} | Get an existing trigger
*TriggerApi* | [**GetTriggerMetrics**](docs/TriggerApi.md#gettriggermetrics) | **GET** /trigger/{triggerID}/metrics | Get metrics associated with certain trigger
*TriggerApi* | [**GetTriggerPlot**](docs/TriggerApi.md#gettriggerplot) | **GET** /trigger/{triggerID}/render | Get rendered plot for trigger
*TriggerApi* | [**GetTriggerState**](docs/TriggerApi.md#gettriggerstate) | **GET** /trigger/{triggerID}/state | Get the trigger state as at last check
*TriggerApi* | [**GetTriggerThrottling**](docs/TriggerApi.md#gettriggerthrottling) | **GET** /trigger/{triggerID}/throttling | Get a trigger with its throttling i.e its next allowed message time
*TriggerApi* | [**GetTriggers**](docs/TriggerApi.md#gettriggers) | **GET** /trigger | get all triggers
*TriggerApi* | [**SearchTriggers**](docs/TriggerApi.md#searchtriggers) | **GET** /trigger/search | Search triggers. Replaces the deprecated `page` path
*TriggerApi* | [**SearchTriggersPage**](docs/TriggerApi.md#searchtriggerspage) | **GET** /trigger/page | Search triggers. Deprecated, use the `search` endpoint instead
*TriggerApi* | [**SetTriggerMaintenance**](docs/TriggerApi.md#settriggermaintenance) | **PUT** /trigger/{triggerID}/setMaintenance | sets metrics and the trigger itself to maintenance mode
*TriggerApi* | [**UpdateTrigger**](docs/TriggerApi.md#updatetrigger) | **PUT** /trigger/{triggerID} | Update existing trigger
*UserApi* | [**GetUser**](docs/UserApi.md#getuser) | **GET** /user | Gets the username of the authenticated user if it is available.
*UserApi* | [**GetUserSettings**](docs/UserApi.md#getusersettings) | **GET** /user/settings | Get the user's contacts and subscriptions.


## Documentation for Models

 - [Model.Contact](docs/Contact.md)
 - [Model.ContactRequest](docs/ContactRequest.md)
 - [Model.ErrorBadRequest](docs/ErrorBadRequest.md)
 - [Model.Event](docs/Event.md)
 - [Model.EventEventMessage](docs/EventEventMessage.md)
 - [Model.EventEventMessageMaintenance](docs/EventEventMessageMaintenance.md)
 - [Model.InlineResponse200](docs/InlineResponse200.md)
 - [Model.InlineResponse2001](docs/InlineResponse2001.md)
 - [Model.InlineResponse20010](docs/InlineResponse20010.md)
 - [Model.InlineResponse20011](docs/InlineResponse20011.md)
 - [Model.InlineResponse20012](docs/InlineResponse20012.md)
 - [Model.InlineResponse2002](docs/InlineResponse2002.md)
 - [Model.InlineResponse2003](docs/InlineResponse2003.md)
 - [Model.InlineResponse2004](docs/InlineResponse2004.md)
 - [Model.InlineResponse2004List](docs/InlineResponse2004List.md)
 - [Model.InlineResponse2005](docs/InlineResponse2005.md)
 - [Model.InlineResponse2006](docs/InlineResponse2006.md)
 - [Model.InlineResponse2007](docs/InlineResponse2007.md)
 - [Model.InlineResponse2008](docs/InlineResponse2008.md)
 - [Model.InlineResponse2009](docs/InlineResponse2009.md)
 - [Model.InlineResponse200Contacts](docs/InlineResponse200Contacts.md)
 - [Model.InlineResponse404](docs/InlineResponse404.md)
 - [Model.InlineResponse500](docs/InlineResponse500.md)
 - [Model.MaintenanceInfo](docs/MaintenanceInfo.md)
 - [Model.MetricState](docs/MetricState.md)
 - [Model.NotificationsList](docs/NotificationsList.md)
 - [Model.NotificationsListList](docs/NotificationsListList.md)
 - [Model.NotificationsListPlotting](docs/NotificationsListPlotting.md)
 - [Model.NotifierState](docs/NotifierState.md)
 - [Model.Subscription](docs/Subscription.md)
 - [Model.SubscriptionPlotting](docs/SubscriptionPlotting.md)
 - [Model.SubscriptionSched](docs/SubscriptionSched.md)
 - [Model.SubscriptionSchedDays](docs/SubscriptionSchedDays.md)
 - [Model.TagStatistics](docs/TagStatistics.md)
 - [Model.Trigger](docs/Trigger.md)
 - [Model.TriggerCheck](docs/TriggerCheck.md)
 - [Model.User](docs/User.md)


## Documentation for Authorization

All endpoints do not require authorization.