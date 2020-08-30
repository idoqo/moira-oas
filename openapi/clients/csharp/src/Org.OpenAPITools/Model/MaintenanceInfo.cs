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
using System.Linq;
using System.IO;
using System.Text;
using System.Text.RegularExpressions;
using System.Collections;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.Runtime.Serialization;
using Newtonsoft.Json;
using Newtonsoft.Json.Converters;
using System.ComponentModel.DataAnnotations;
using OpenAPIDateConverter = Org.OpenAPITools.Client.OpenAPIDateConverter;

namespace Org.OpenAPITools.Model
{
    /// <summary>
    /// MaintenanceInfo
    /// </summary>
    [DataContract]
    public partial class MaintenanceInfo :  IEquatable<MaintenanceInfo>, IValidatableObject
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="MaintenanceInfo" /> class.
        /// </summary>
        /// <param name="setupUser">setupUser.</param>
        /// <param name="setupTime">setupTime.</param>
        /// <param name="removeUser">removeUser.</param>
        /// <param name="removeTime">removeTime.</param>
        public MaintenanceInfo(string setupUser = default(string), int setupTime = default(int), string removeUser = default(string), int removeTime = default(int))
        {
            this.SetupUser = setupUser;
            this.SetupTime = setupTime;
            this.RemoveUser = removeUser;
            this.RemoveTime = removeTime;
        }
        
        /// <summary>
        /// Gets or Sets SetupUser
        /// </summary>
        [DataMember(Name="setup_user", EmitDefaultValue=false)]
        public string SetupUser { get; set; }

        /// <summary>
        /// Gets or Sets SetupTime
        /// </summary>
        [DataMember(Name="setup_time", EmitDefaultValue=false)]
        public int SetupTime { get; set; }

        /// <summary>
        /// Gets or Sets RemoveUser
        /// </summary>
        [DataMember(Name="remove_user", EmitDefaultValue=false)]
        public string RemoveUser { get; set; }

        /// <summary>
        /// Gets or Sets RemoveTime
        /// </summary>
        [DataMember(Name="remove_time", EmitDefaultValue=false)]
        public int RemoveTime { get; set; }

        /// <summary>
        /// Returns the string presentation of the object
        /// </summary>
        /// <returns>String presentation of the object</returns>
        public override string ToString()
        {
            var sb = new StringBuilder();
            sb.Append("class MaintenanceInfo {\n");
            sb.Append("  SetupUser: ").Append(SetupUser).Append("\n");
            sb.Append("  SetupTime: ").Append(SetupTime).Append("\n");
            sb.Append("  RemoveUser: ").Append(RemoveUser).Append("\n");
            sb.Append("  RemoveTime: ").Append(RemoveTime).Append("\n");
            sb.Append("}\n");
            return sb.ToString();
        }
  
        /// <summary>
        /// Returns the JSON string presentation of the object
        /// </summary>
        /// <returns>JSON string presentation of the object</returns>
        public virtual string ToJson()
        {
            return JsonConvert.SerializeObject(this, Formatting.Indented);
        }

        /// <summary>
        /// Returns true if objects are equal
        /// </summary>
        /// <param name="input">Object to be compared</param>
        /// <returns>Boolean</returns>
        public override bool Equals(object input)
        {
            return this.Equals(input as MaintenanceInfo);
        }

        /// <summary>
        /// Returns true if MaintenanceInfo instances are equal
        /// </summary>
        /// <param name="input">Instance of MaintenanceInfo to be compared</param>
        /// <returns>Boolean</returns>
        public bool Equals(MaintenanceInfo input)
        {
            if (input == null)
                return false;

            return 
                (
                    this.SetupUser == input.SetupUser ||
                    (this.SetupUser != null &&
                    this.SetupUser.Equals(input.SetupUser))
                ) && 
                (
                    this.SetupTime == input.SetupTime ||
                    (this.SetupTime != null &&
                    this.SetupTime.Equals(input.SetupTime))
                ) && 
                (
                    this.RemoveUser == input.RemoveUser ||
                    (this.RemoveUser != null &&
                    this.RemoveUser.Equals(input.RemoveUser))
                ) && 
                (
                    this.RemoveTime == input.RemoveTime ||
                    (this.RemoveTime != null &&
                    this.RemoveTime.Equals(input.RemoveTime))
                );
        }

        /// <summary>
        /// Gets the hash code
        /// </summary>
        /// <returns>Hash code</returns>
        public override int GetHashCode()
        {
            unchecked // Overflow is fine, just wrap
            {
                int hashCode = 41;
                if (this.SetupUser != null)
                    hashCode = hashCode * 59 + this.SetupUser.GetHashCode();
                if (this.SetupTime != null)
                    hashCode = hashCode * 59 + this.SetupTime.GetHashCode();
                if (this.RemoveUser != null)
                    hashCode = hashCode * 59 + this.RemoveUser.GetHashCode();
                if (this.RemoveTime != null)
                    hashCode = hashCode * 59 + this.RemoveTime.GetHashCode();
                return hashCode;
            }
        }

        /// <summary>
        /// To validate all properties of the instance
        /// </summary>
        /// <param name="validationContext">Validation context</param>
        /// <returns>Validation Result</returns>
        IEnumerable<System.ComponentModel.DataAnnotations.ValidationResult> IValidatableObject.Validate(ValidationContext validationContext)
        {
            yield break;
        }
    }

}
