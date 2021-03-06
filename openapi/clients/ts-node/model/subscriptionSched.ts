/**
 * Moira Alert
 * This is an API description for [Moira Alert project](https://moira.readthedocs.io/en/latest/overview.html). Please check <https://github.com/moira-alert/>
 *
 * The version of the OpenAPI document: 2.5.1.48
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

import { RequestFile } from '../api';
import { SubscriptionSchedDays } from './subscriptionSchedDays';

export class SubscriptionSched {
    'days'?: Array<SubscriptionSchedDays>;
    /**
    * Timezone offset in seconds (wrt GMT)
    */
    'tzOffset'?: number;
    'startOffset'?: number;
    'endOffset'?: number;

    static discriminator: string | undefined = undefined;

    static attributeTypeMap: Array<{name: string, baseName: string, type: string}> = [
        {
            "name": "days",
            "baseName": "days",
            "type": "Array<SubscriptionSchedDays>"
        },
        {
            "name": "tzOffset",
            "baseName": "tzOffset",
            "type": "number"
        },
        {
            "name": "startOffset",
            "baseName": "startOffset",
            "type": "number"
        },
        {
            "name": "endOffset",
            "baseName": "endOffset",
            "type": "number"
        }    ];

    static getAttributeTypeMap() {
        return SubscriptionSched.attributeTypeMap;
    }
}

